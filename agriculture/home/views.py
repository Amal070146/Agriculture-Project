from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Cold_storage, Retailer, Farmer
import datetime
from .templates import *

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                if user.occupation == 'farmer':
                    return redirect('fam_coma.html')
                elif user.occupation == 'retailer':
                    return redirect(retailers_table)
                else:
                    return redirect(cold_storage)
            else:
                data = {'status':"Incorrect Password!!!"}
                print(data)
                return render(request, 'login.html', context=data)
        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            print(data)
            return render(request, 'signup.html', context=data)
    else:
        return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        adr = request.POST.get('adr')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        occupation = request.POST.get('occupation')
        if(password == confirm_password):
            user = User(uid=uid,occupation=occupation,first_name=first_name,last_name=last_name,adr=adr,mobile=mobile,age=age,gender=gender,email=email,password=password)
            user.save()
        return render(request, 'signup.html')
    if request.method == 'GET':
        occupation = request.GET['occupation']
        return render(request, 'signup.html', {'occupation': occupation})
        
            
#Cold Storage Management team

def cold_storage(request):
    # cold_storage = Cold_storage
    # cold_storage.save()
    return render(request, 'cold_storage.html')

#Farmers Management system

def farmers_table(request):
    return render(request, 'farmers_table.html')

#Farmers Management system

def retailers_table(request):
    return render(request, 'retailers_table.html')