"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from APP.models import User
def Login(request):
        return render(request,'login.html')
        ''''''
def Authenticate_User(request):
        username=request.POST['username']
        password=request.POST['password']
        department=request.POST['department']
        user=authenticate(request,username=username,password=password)
        print()
        if user is not None:
            print(user.department_name)
            if user.department_name==department:
                  login(request,user)
                  print('Logined')    
                  print(user)
                  return HttpResponseRedirect('/')
            else:
                return render(request,'login.html',{'Invalid_Department':'You Have Selected Wrong Department'})
        else:
            print('Not Logined I think there is something problem')
            return render(request,'login.html')   
def Registration_Form(request):
    return render(request,'register.html')


def Register_User(request):
    username=request.POST['username']
    password=request.POST['password']
    department=request.POST['department']
    user=User.objects.create_user(username=username,password=password)
    user.department_name=department
    user.save()
    return HttpResponseRedirect('login')

def Home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return HttpResponseRedirect('login')    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',Login,name='login Page'),
    path('',Home,name='Index Page'),
    path('authenticate_user',Authenticate_User,name='User Authentication'),
    path('register',Registration_Form,name='Show Registeraton Form'),
    path('register_user',Register_User,name='RegisterUser')
]
