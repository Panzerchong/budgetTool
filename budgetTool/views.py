from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RateTable, Project,BoM,Service,Sales,BillOfMaterials
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
    custom=BillOfMaterials.objects.filter(project_id=pk,category="CUSTOM HARDWARE")
    uma=BillOfMaterials.objects.filter(project_id=pk,category="UMA SOLUTION")
    controls=BillOfMaterials.objects.filter(project_id=pk,category="CONTROLS")
    software=BillOfMaterials.objects.filter(project_id=pk,category="SOFTWARE")
    protection=BillOfMaterials.objects.filter(project_id=pk,category="PROTECTION PLANS")

    #service
    general_service=Service.objects.filter(project_id=pk,category="GENERAL PROJECT")
    hardware_service=Service.objects.filter(project_id=pk,category="HARDWARE DEVELOPMENT")
    software_service=Service.objects.filter(project_id=pk,category="SOFTWARE DEVELOPMENT")
    implementation=Service.objects.filter(project_id=pk,category="IMPLEMENTATION")
    factory_test_service=Service.objects.filter(project_id=pk,category="FACTORY ACCEPTANCE TEST")
    shipping=Service.objects.filter(project_id=pk,category="SHIPPING")
    installation=Service.objects.filter(project_id=pk,category="INSTALLATION")
    site_test_service=Service.objects.filter(project_id=pk,category="SITE ACCEPTANCE TEST")
    training_service=Service.objects.filter(project_id=pk,category="TRAINING")


    context={
        "table":table,
        "project":project,
        "custom":custom,
        "uma":uma,
        "controls":controls,
        "software":software,
        "protection":protection,

        'general_service':        general_service,
        'hardware_service':        hardware_service,
        'software_service':        software_service,
        'implementation' :       implementation,
        'factory_test_service':        factory_test_service,
        'shipping':        shipping,
        'installation':        installation,
        'site_test_service' :       site_test_service,
        'training_service':      training_service,
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
    form=ServiceModelForm()
    if request.method =="POST":
        print(project.name)
        form=ServiceModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("created a new service")
            return redirect(f'/budgetTool/{project.pk}')
    context={
        "form":ServiceModelForm(initial={'project': project})
    }
    return render(request,"budgetTool/create_service.html",context)


def service_update(request,pk,fk):
    item=Service.objects.get(id=pk,project_id=fk)
    form=ServiceModelForm(instance=item)

    if request.method =="POST":
        print("received")
        form=ServiceModelForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            print("edit a item")
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
