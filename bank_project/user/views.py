from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('profile')
        else:
            messages.info(request,"Check username and password")
            code=0
            return render(request,'login.html',{"code":code})

    return render(request,'login.html')

def register(request):
    try:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            if username != "" and password != "" and cpassword != "":
                if password == cpassword:
                    if User.objects.filter(username=username).exists():
                        messages.info(request,"username exists")
                        code = 0
                        return redirect('user:register',)
                    else:
                        user = User.objects.create_user(username=username,password=password)
                        messages.info(request,"user created")
                        code = 1
                        return render(request,'login.html',{"code":code})
                else:
                    messages.info(request,"password mismatched")
                    return redirect('register')
            else:
                messages.info(request,"fill all details")
    except:
        return render(request,'register.html',)
    return render(request,'register.html',)

def logout(request):
    auth.logout(request)
    return redirect('/')
