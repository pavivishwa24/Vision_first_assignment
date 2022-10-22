from django.shortcuts import render,redirect
from .models import UserForm as user_data,Company
from .forms import UserForm,CompanyCreateForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def show(request):
    return render(request,"home.html")

def register(request):
    title="User Registration"
    form= UserForm()
    if request.method == 'POST':
        form= UserForm(request.POST or None)
        if form.is_valid():
            # p = UserForm(name=name,username=username,password=password,mobile=mobile,email=email)           
            form.save()
            print("form is",form)
            data = form.cleaned_data
            field = data['username']
            print("form is",field)
            response = HttpResponse("Logged in successfull")
            response.set_cookie('logged_user', field)
            return response
            return render(request,'ack.html',{"title":"Registered successfully"})


    context={
        "title":title,
        "form":form,

    }
    return render(request,'register.html',{'form':form})


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            res=user_data.objects.filter(username=username,password=password)[0]
            if res:
                print("res is",res.role)
                # if role admin redirect to admin
                if res.role=="IT_ADMIN":
                    response =redirect("admin")
                    return response
                    
                print("yoo res is successful")
                response = HttpResponse("Logged in successfull")
                data=Company.objects.filter(created_by=res.username)
                message=""
                cform = CompanyCreateForm()
                # response = redirect(request,'companies.html',{"message":message,"data":data,"form":cform} )
                response =redirect("companies")
                response.set_cookie('logged_user', res.username)
                return response
            else:
                return response
        except:
            return HttpResponse("wrong credentials")
    return render(request,"login.html",context)

    
def success(request):
    context = {}
    context['user'] = request.user
    return render(request,"auth/success.html",context)




def success(request):
    pass


def companies(request):
    
    message=""
    current_user= request.COOKIES.get('logged_user')
    data=Company.objects.filter(created_by=current_user)
    print("got data as ",data)
    if request.method == 'POST':
        form = Company()
        form.name = request.POST['name']
        form.address = request.POST['address']
        form.created_by = current_user
        form.status = 0
        c=form.save()
    # c=Company.objects.create(name,address,created_by,status)
        if c:
            message="Created Successfully"
            return render(request,'companies.html',{"message":message,"data":data})
    form=CompanyCreateForm()
    return render(request,'companies.html',{"message":message,"data":data,"form":form})

def admin(request):
    current_user= request.COOKIES.get('logged_user')
    if current_user=="admin":
        data=Company.objects.filter()
        message=""
        if request.method == 'POST':
            form = Company()
            form.name = request.POST['name']
            form.address = request.POST['address']
            form.created_by = "admin"
            form.status = 0
            c=form.save()
            if c:
                message="Created Successfully"
                return render(request,'admin.html',{"message":message,"data":data})
        form=CompanyCreateForm()
        return render(request,'admin.html',{"message":message,"data":data,"form":form})
    else:
        response =redirect("login")
        return response

def edit(request,id):
    c=Company.objects.get(id=id)
    print(c)
    form=CompanyCreateForm(request.POST or None, instance=c)
    print("------------form is ",form)
    if request.method == 'POST' and form.is_valid():

        form.save()
        return HttpResponseRedirect(reverse('admin'))
    return render(request,'edit.html',{"form":form})
    



def approve(request,id):
    c=Company.objects.get(id=id)
    c.status=1
    c.save()
    response =redirect("admin")
    return response


def delete(request,id):
    c=Company.objects.get(id=id)
    print("---------------c is",c)
    c.delete()
    # form=CompanyCreateForm()
    # data=Company.objects.filter()
    response =redirect("admin")
    return response


def delete(request,id):
    response = HttpResponse("Deleting the cookie which is set")  
    response.delete_cookie('logged_user','Updated Successfully')  
    response =redirect("admin")
    return response