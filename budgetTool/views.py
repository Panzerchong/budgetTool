from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RateTable, Project,BoM,Service,Sales
from .forms import ProjectForm


def budget_list(request):
    projects=Project.objects.all()
    context={
        "projects": projects,
    }
    return render(request, 'budgetTool/budget_list.html',context)

def budget_detail(request,pk):
    project=Project.objects.get(id=pk)
    context={
        "project":project
    }
    return render(request, 'budgetTool/budget_detail.html',context)


def create_project(request):
    form=ProjectForm()
    if request.method =="POST":
        print("received")
        form=ProjectForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            quote=form.cleaned_data['quote']
            bom=BoM.objects.first()
            service=Service.objects.first()

            Project.objects.create(
                name=name,
                quote=quote,
                bom=bom,
                service=service
            )
            print("created a new project")
            return redirect("/budgetTool")

    context={
        "form":ProjectForm()
    }
    return render(request,"budgetTool/create_project.html",context)

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
