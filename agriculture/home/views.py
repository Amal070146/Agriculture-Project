from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
import datetime
from .templates import *

# Create your views here.

def home(request):
    return render( request,'home.html')

def farmers_table(request):
    # grocery_list = {'grocery':Grocery.objects.all()}
    return render( request,'farmers-table.html')

def login(request):
    return render( request,'login.html')

def signup(request):
    return render( request,'signup.html')

def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)

            if user.password == password:
                request.session['uname'] = name
                return user_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'registration.html',context=data)

        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")
