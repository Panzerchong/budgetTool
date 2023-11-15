from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RateTable, Project,BoM,Service,Sales,BillOfMaterials,ServiceCategory,BOMCategory
from .forms import ProjectForm, ProjectModelForm,BillModelForm,ServiceModelForm


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
    # custom=BillOfMaterials.objects.filter(project_id=pk,category="CUSTOM HARDWARE")
    # uma=BillOfMaterials.objects.filter(project_id=pk,category="UMA SOLUTION")
    # controls=BillOfMaterials.objects.filter(project_id=pk,category="CONTROLS")
    # software=BillOfMaterials.objects.filter(project_id=pk,category="SOFTWARE")
    # protection=BillOfMaterials.objects.filter(project_id=pk,category="PROTECTION PLANS")
    bom_category=BOMCategory.objects.filter(project_BOM_category__isnull=False).distinct().order_by('index')

    #service
    service=Service.objects.filter(project_id=pk)
    #filter out category not used
    service_category=ServiceCategory.objects.filter(project_service_category__isnull=False).distinct().order_by('index')

    context={
        "table":table,
        "project":project,
        "service": service,
        "bom":bom,
        "service_category": service_category,
        "existing_bom_category":bom_category,
        # "custom":custom,
        # "uma":uma,
        # "controls":controls,
        # "software":software,
        # "protection":protection,
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
            return redirect("/budgetTool")
    context={
        "project":project,
        "form":form,
    }

    return render(request,"budgetTool/project_update.html",context)

def project_delete(request,pk):
    project=Project.objects.get(id=pk)
    project.delete()
    return redirect("/budgetTool")

def create_bom(request,pk):
    project=Project.objects.get(id=pk)
    form=BillModelForm()
    if request.method =="POST":
        print(project.name)
        form=BillModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            form.save()
            print("created a new BOM")
            return redirect(f'/budgetTool/{project.pk}')
    context={
        "form":BillModelForm(initial={'project': project})
    }
    return render(request,"budgetTool/create_bom.html",context)


def bom_update(request,pk,fk):
    item=BillOfMaterials.objects.get(id=pk,project_id=fk)
    form=BillModelForm(instance=item)

    if request.method =="POST":
        print("received")
        form=BillModelForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            print("edit a item")
            return redirect(f'/budgetTool/{item.project_id}')
    context={
        "item":item,
        "form":form,
    }
    return render(request,"budgetTool/bom_update.html",context)

def create_service(request,pk):
    project=Project.objects.get(id=pk)
    rate_table=RateTable.objects.all()
    form=ServiceModelForm()
    if request.method =="POST":
        print(project.name)
        form=ServiceModelForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            name=data['name']
            category=data['category']
            type=data['type']
            hours_estimated=data['hours_estimated']
            hours_worked=data['hours_worked']
            rate_list=data['rate_list']
            rate_cost=data['rate_cost']
            travel_actual=data['travel_actual']
            notes=data['notes']
            
            if rate_list == -1:
                for item in rate_table:
                    if type == item.type:                  
                        rate_list=item.list
            if rate_cost == -1:
                 for item in rate_table:
                    if type == item.type:
                        rate_cost=item.cost

            #calculated field value
            print(rate_cost+rate_list)
            hours_adjusted=hours_estimated*(1+project.adjust_Service)
            travel_estimate=hours_estimated*project.travel_weekly/40
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
                notes=notes,
                project=project,
                hours_adjusted=hours_adjusted,
                travel_estimate=travel_estimate,
                sub_total_list=sub_total_list,
                sub_total_adjusted_list=sub_total_adjusted_list,
                sub_total_cost_est=sub_total_cost_est,
                sub_total_adjusted_cost_est=sub_total_adjusted_cost_est,
                cost_actual=cost_actual,
            )
            return redirect(f'/budgetTool/{project.pk}')
    context={
        "form":ServiceModelForm(initial={'project': project})
    }
    return render(request,"budgetTool/create_service.html",context)

# def create_service(request,pk):
#     project=Project.objects.get(id=pk)
#     form=ServiceModelForm()
#     if request.method =="POST":
#         print(project.name)
#         form=ServiceModelForm(request.POST)
#         if form.is_valid():
#             rate_list=500
#             rate_cost=159
#             form.save()
#             print("created a new service")
#             return redirect(f'/budgetTool/{project.pk}')
#     context={
#         "form":ServiceModelForm(initial={'project': project})
#     }
#     return render(request,"budgetTool/create_service.html",context)


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
