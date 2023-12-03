from gettext import translation
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse,QueryDict
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RateTable, Project,BoM,Service,Sales,BillOfMaterials,ServiceCategory,BOMCategory
from .forms import OrderForm, ProjectForm, ProjectModelForm,BillModelForm,ServiceModelForm
import json
from django.views.decorators.http import require_http_methods


def budget_list(request):
    projects=Project.objects.all()
    context={
        "projects": projects,
    }
    return render(request, 'budgetTool/budget_list.html',context)

def rate_table(request):
    table=RateTable.objects.all()
    context={
        "table": table,
    }
    return render(request,'budgetTool/rate_table.html',context)

def budget_detail(request,pk):
    project=Project.objects.get(id=pk)
    table=RateTable.objects.all()
    bom=BillOfMaterials.objects.filter(project_id=pk)
    bom_category=BOMCategory.objects.filter(project_BOM_category__isnull=False).distinct().order_by('index')

    #service
    service=Service.objects.filter(project_id=pk)
    #filter out category not used
    service_category=ServiceCategory.objects.filter(project_service_category__isnull=False).distinct().order_by('index')


    bomForm=BillModelForm()
    if request.method =="POST":
        print("received")
        bomForm=BillModelForm(request.POST)
        if bomForm.is_valid():
            bomForm.save()
            print("created a new bom item")
            return JsonResponse({'status': 'success'})
        else:
            print("invalid form")
            errors = bomForm.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)

    context={
        "table":table,
        "project":project,
        "service": service,
        "bom":bom,
        "service_category": service_category,
        "existing_bom_category":bom_category,
        "bomForm":BillModelForm(),
    }
    return render(request, 'budgetTool/budget_detail.html',context)


def create_project(request):
    form=ProjectModelForm()
    if request.method =="POST":
        print("received")
        form=ProjectModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("created a new project")
            return redirect("/budgetTool")

    context={
        "form":ProjectModelForm()
    }
    return render(request,"budgetTool/create_project.html",context)

def project_update(request,pk):
    project=Project.objects.get(id=pk)
    form=ProjectModelForm(instance=project)
    if request.method =="POST":
        print("received")
        form=ProjectModelForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            print("created a new project")
            return redirect(f'/budgetTool/{project.pk}')
    context={
        "project":project,
        "form":form,
    }

    return render(request,"budgetTool/project_update.html",context)

def project_delete(request,pk):
    project=Project.objects.get(id=pk)
    project.delete()
    return redirect("/budgetTool")

def create_bom(request, pk):
    project = Project.objects.get(id=pk)
    
    if request.method == "POST":
        bomForm = BillModelForm(request.POST)
        request_data = request.POST.copy()
        mutable_data = QueryDict(mutable=True)
        mutable_data.update(request_data)
        mutable_data.appendlist('project', project.pk)
        bomForm = BillModelForm(mutable_data)
        if bomForm.is_valid():
            bomForm.save()
            print("created a new BOM")
            return HttpResponse("Saved")
    bomForm = BillModelForm(initial={'project': project})
    context = {"bomForm": bomForm, "project": project}
    return render(request, "budgetTool/partials/bomForm.html", context)

def bom_update(request,pk,fk):
    item=BillOfMaterials.objects.get(id=pk,project_id=fk)
    form=BillModelForm(instance=item)

    if request.method =="POST":
        print("received")
        form=BillModelForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            print("edit a item")
            return HttpResponse("BOM updated")
    context={
        "item":item,
        "form":form,
    }
    return render(request,"budgetTool/partials/bomForm.html",context)

def create_service(request,pk):
    project=Project.objects.get(id=pk)
    rate_table=RateTable.objects.all()
    form=ServiceModelForm()
    if request.method =="POST":
        print(project.name)
        form=ServiceModelForm(request.POST,initial={'project': project})
        print(form.data)

        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data['name']
            category=data['category']
            type=data['type']
            hours_estimated=data['hours_estimated']
            hours_worked=data['hours_worked']
            rate_list=data['rate_list']
            rate_cost=data['rate_cost']
            travel_actual=data['travel_actual']
            
            if rate_list == -1:
                for item in rate_table:
                    if type == item.type:                  
                        rate_list=item.list
            if rate_cost == -1:
                 for item in rate_table:
                    if type == item.type:
                        rate_cost=item.cost

            #calculated field value
            print(project.adjust_Service)
            if "On Site" in type:
                travel_estimate=hours_estimated*project.travel_weekly/40
            else:
                travel_estimate=0

            hours_adjusted=hours_estimated*(1+project.adjust_Service)
            sub_total_list=hours_estimated*rate_list+travel_estimate
            sub_total_adjusted_list=hours_adjusted*rate_list+travel_estimate
            sub_total_cost_est=hours_estimated*rate_cost+travel_estimate
            sub_total_adjusted_cost_est=hours_adjusted*rate_cost+travel_estimate
            cost_actual=hours_worked*rate_cost+travel_actual

            print(f'rate_list: {rate_cost}')
            Service.objects.create(   
                name=name,
                category=category,
                type=type,
                hours_estimated=hours_estimated,
                hours_worked=hours_worked,
                rate_list=rate_list,
                rate_cost=rate_cost,
                travel_actual=travel_actual,
                project=project,
                hours_adjusted=hours_adjusted,
                travel_estimate=travel_estimate,
                sub_total_list=sub_total_list,
                sub_total_adjusted_list=sub_total_adjusted_list,
                sub_total_cost_est=sub_total_cost_est,
                sub_total_adjusted_cost_est=sub_total_adjusted_cost_est,
                cost_actual=cost_actual,
            )
            return HttpResponse("Service Saved")
    context={
        "form":ServiceModelForm(initial={'project': project},),
        "project":project,
    }
    return render(request,"budgetTool/partials/serviceForm.html",context)


def service_update(request,pk,fk):
    item=Service.objects.get(id=pk,project_id=fk)
    form=ServiceModelForm(instance=item)
    rate_table=RateTable.objects.all()

    if request.method =="POST":
        print("received")
        form=ServiceModelForm(request.POST,instance=item)
        if form.is_valid():
            data=form.cleaned_data
            name=data['name']
            category=data['category']
            type=data['type']
            hours_estimated=data['hours_estimated']
            hours_worked=data['hours_worked']
            rate_list=0
            rate_cost=0
            travel_actual=data['travel_actual']
            notes=data['notes']

            for service in rate_table:
                if type == service.type:
                   
                    rate_list=service.list
                    rate_cost=service.cost

            Service.objects.update(
                name=name,
                category=category,
                type=type,
                hours_estimated=hours_estimated,
                hours_worked=hours_worked,
                rate_list=rate_list,
                rate_cost=rate_cost,
                travel_actual=travel_actual,
                notes=notes,
                )
            print("edit an item")
            return redirect(f'/budgetTool/{item.project_id}')
    context={
        "item":item,
        "form":form,
    }
    return render(request,"budgetTool/service_update.html",context)

def bomSave(request,pk):
    project=Project.objects.get(id=pk)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        form = BillModelForm(data)

        if form.is_valid():
            new_item = form.save()
            return JsonResponse({'id': new_item.id})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'})


def bom(request,pk):
    bom=BillOfMaterials.objects.get(id=pk)
    context={
        "bom": bom,
    }
    return render(request,'budgetTool/bom.html',context)

def service(request):
    rate_table=RateTable.objects.all()
    context={
        "rate_table": rate_table,
    }
    return render(request,'budgetTool/rate_table.html',context)
# def home(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']

#         user=authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request,user)
#             messages.success(request,"You have been logged in!")
#             return redirect('home')
#         else:
#             messages.success(request,"There was an error log in. Please try again...")
#             return redirect('index')
#     else:
#         return render(request, 'index.html',{})

# def login_user(request):
#     pass

# def logout_user(request):
#     logout(request)
#     messages.success(request,"You have been logged out...")
#     return redirect('index')

# def rate_table(request):
#     table=RateTable.objects.all()

#     return messages.success(request,"it's ratetable\n")


def editProject(request,pk):
    project=Project.objects.get(id=pk)

    if request.method == 'POST':
        if request.POST.get('name'):
            project.name=request.POST.get('name','')
        if request.POST.get('quote_BOM'):
            project.quote_BOM=request.POST.get('quote_BOM','')
        if request.POST.get('quote_Service'):
            project.quote_Service=request.POST.get('quote_Service','')
        if request.POST.get('adjust_Service'):
            project.adjust_Service=request.POST.get('adjust_Service','')
        if request.POST.get('adjust_BOM'):
            project.adjust_BOM=request.POST.get('adjust_BOM','')
        if request.POST.get('travel_weekly'):
            project.travel_weekly=request.POST.get('travel_weekly','')
        project.save()
        return HttpResponse("Project updated successfully")
    
    ProjectForm=ProjectModelForm(instance=project)
    context = {"ProjectForm": ProjectForm, "project": project}
    if request.GET.get('quote_BOM'):
        return render(request,'budgetTool/partials/project/editProjectBomQuote.html',context)
    elif request.GET.get('name'):
        return render(request,'budgetTool/partials/project/editProjectName.html',context)
    elif request.GET.get('quote_Service'):
        return render(request,'budgetTool/partials/project/editProjectServiceQuote.html',context)
    elif request.GET.get('adjust_Service'):
        return render(request,'budgetTool/partials/project/editProjectServiceAdjust.html',context)
    elif request.GET.get('adjust_BOM'):
        return render(request,'budgetTool/partials/project/editProjectBomAdjust.html',context)
    elif request.GET.get('travel_weekly'):
        return render(request,'budgetTool/partials/project/editProjectTravel.html',context)
    else:
        return HttpResponse("Project update")
    

def bom_edit(request, pk, fk):
    item = get_object_or_404(BillOfMaterials, id=pk, project_id=fk)

    if request.method == "POST":
        request_data = request.POST.copy()
        request_data['project'] = fk  # Add project to POST data
        bomForm = BillModelForm(request_data, instance=item)

        if bomForm.is_valid():
            bomForm.save()
            return HttpResponse("BOM updated successfully")

    else:
        bomForm = BillModelForm(instance=item)

    context = {
        "item": item,
        "bomForm": bomForm,
    }

    return render(request, "budgetTool/partials/bomFormEdit.html", context)

def bom_delete(request,pk):
    bom=BillOfMaterials.objects.get(id=pk)
    bom.delete()
    

def service_edit(request, pk, fk):
    item = get_object_or_404(Service, id=pk, project_id=fk)

    if request.method == "POST":
        request_data = request.POST.copy()
        request_data['project'] = fk  # Add project to POST data
        form = ServiceModelForm(request_data, instance=item)

        if form.is_valid():
            form.save()
            return HttpResponse("BOM updated successfully")

    else:
        form = ServiceModelForm(instance=item)

    context = {
        "item": item,
        "form": form,
    }
    return render(request, "budgetTool/partials/serviceFormEdit.html", context)

def service_delete(request,pk):
    service=Service.objects.get(id=pk)
    service.delete()

def service_order(request):
    form=OrderForm(request.POST)

    if form.is_valid():
        ordered_ids = form.cleaned_data["ordering"].split(',')
        print(ordered_ids)
        current_order = 1
        for lookup_id in ordered_ids:
            if lookup_id.isdigit() and lookup_id != "0":
                service = Service.objects.get(id=lookup_id)
                service.order = current_order
                service.save(update_fields=["order"])
                print(f'what is Service: {service.order}')
                current_order += 1
        return HttpResponse("Order updated successfully")

    