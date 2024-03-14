from django.shortcuts import render
from .models import *
from django.shortcuts import redirect


# Create your views here.

def home(request):
    
    return render(request,"home.html")

def addUser(request):
    if(request.method=="POST"):
        if request.POST['user_id']!="":
            user_id = request.POST['user_id']
            select_user = Users.objects.get(id=user_id)
            select_user.name = request.POST['name']
            select_user.email = request.POST['email']
            select_user.password = request.POST['password']
            select_user.save()
            return redirect('viewUsers')
            
        else:
            Users.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                password = request.POST['password']
            )
            return redirect('viewUsers')

def viewUsers(request):
    all_user = Users.objects.all()
    return render(request,"view_users.html",{"all_user":all_user})

def deleteUser(request,user_id):
    select_user = Users.objects.get(id=user_id)
    select_user.delete()
    return redirect('viewUsers')

    # return viewUsers(request)

def editUser(request,user_id):
    select_user = Users.objects.get(id=user_id)
    return render(request,"home.html",{"select_user":select_user})

    

