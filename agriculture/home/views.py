from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Cold_storage
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
                request.session['uid'] = user.uid
                if user.occupation == 'farmer':
                    return redirect('/farmers_table/')
                elif user.occupation == 'retailer':
                    return redirect('/retailers_table/')
                else:
                    return redirect("/cold_storage/")
            else:
                data = {'status':"Incorrect Password!!!"}
                print(data)
                return render(request, 'login.html', context=data)
        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            print(email,password)
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
        cs_name = request.POST.get('cs_name')
        if(password == confirm_password):
            if occupation == 'cold storage':
                print(cs_name)
                user = User(uid=uid, occupation=occupation, first_name=first_name, last_name=last_name, adr=adr,
                            mobile=mobile, age=age, gender=gender, email=email, password=password, cs_name=cs_name)
            else:
                user = User(uid=uid, occupation=occupation, first_name=first_name, last_name=last_name, adr=adr, mobile=mobile, age=age, gender=gender, email=email, password=password)
            user.save()
        return render(request, 'signup.html')
    if request.method == 'GET':
        occupation = request.GET['occupation']
        return render(request, 'signup.html', {'occupation': occupation})
        
            
#Cold Storage Management team

def cold_storage(request):
    uid = request.session['uid']
    current_user = User.objects.get(uid=uid)
    if request.method == "POST":
        add = request.POST.get('add')
        delete = request.POST.get('delete')
        pname = request.POST.get('pname')
        print(add,delete)
        if (add == None and delete == None):
            max_str = request.POST.get('max_str')
            avl_str = request.POST.get('avl_str')
            pname = request.POST.get('pname')
            if (max_str==None and avl_str==None):
                cs2 = Cold_storage.objects.get(cs_own = uid, cs_pname = pname)
                cs2.delete()
            elif avl_str <= max_str:
                print('saved pro')
                cs = Cold_storage(cs_own=current_user, cs_pname=pname, cs_max_str=max_str, cs_avl_str=avl_str)
                cs.save()
            else:
                data = {'status': "size of max_str should be greater than avl_str"}

        else:
            cs1 = Cold_storage.objects.get(cs_own=uid, cs_pname=pname)
            cs1.cs_avl_str = cs1.cs_avl_str + int(delete) - int(add)
            print('saved add')
            if cs1.cs_avl_str <= cs1.cs_max_str:
                cs1.save()

    my_cold_storage = Cold_storage.objects.filter(cs_own = uid)
    context = {"data":my_cold_storage}
    return render(request, 'cold_storage.html', context = context)


#Farmers Management system

def farmers_table(request):
    cold_storages = User.objects.filter(occupation='cold storage')
    product_list = []
    for cs in cold_storages:
        product_list.append(Cold_storage.objects.filter(cs_own=cs))
    return render(request, 'fam_coma.html', {"cold_storages":cold_storages,'products':product_list})


#Farmers Management system

def retailers_table(request):
    cold_storages = User.objects.filter(occupation='cold storage')
    product_list = []
    for cs in cold_storages:
        product_list.append(Cold_storage.objects.filter(cs_own=cs))
    return render(request, 'retailers_table.html',{"cold_storages":cold_storages,'products':product_list})
    
