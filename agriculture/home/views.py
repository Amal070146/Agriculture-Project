from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
import datetime
from .templates import *

# Create your views here.

def home(request):
    return render( request,'home.html')

def farmers_table(request):
    # grocery_list = {'grocery':Grocery.objects.all()}
    return render( request,'farmers_table.html')

def retailers_table(request):
    # grocery_list = {'grocery':Grocery.objects.all()}
    return render( request,'retailers_table.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)

            if user.password == password:
                if user.occupation == 'farmer':
                    return redirect(farmers_table)
                elif user.occupation == 'retailer':
                    return redirect(retailers_table)
                else:
                    request.session['uname'] = name
                    return (request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'login.html',context=data)

        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            return render(request,'signup.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")


# def signup(request):
#     user = User()
#     if request.method == 'POST':
#         user.uid = request.POST.get('uid')
#         User.first_name = request.POST.get('first_name')
#         user.last_name = request.POST.get('last_name')
#         user.adr = request.POST.get('adr')
#         user.ph_no = request.POST.get('ph_no')
#         user.age = request.POST.get('age')
#         user.gender = request.POST.get('gender')
#         user.email = request.POST.get('email')
#         user.password = request.POST.get('password')
#     if request.method == 'GET':
#         user.occupation = request.GET['occupation']
#     user.save()
#     return render( request,'signup.html')

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

        if(password == confirm_password):
            user = User(uid=uid,first_name=first_name,last_name=last_name,adr=adr,mobile=mobile,age=age,gender=gender,email=email,password=password)
            if request.method == 'GET':
                user.occupation = request.GET['occupation']
            user.save()
    return render(request, 'signup.html')