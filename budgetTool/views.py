from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RateTable, Project,BoM,Service,Sales
from .forms import ProjectForm, ProjectModelForm


def budget_list(request):
    projects=Project.objects.all()
    context={
        "projects": projects,
    }
    return render(request, 'budgetTool/budget_list.html',context)

def rate_table(request):
    rate_table=RateTable.objects.all()
    context={
        "rate_table": rate_table,
    }
    return render(request,'budgetTool/rate_table.html',context)

def budget_detail(request,pk):
    project=Project.objects.get(id=pk)
    context={
        "project":project
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
