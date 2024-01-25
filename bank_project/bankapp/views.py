from django.contrib import messages

from .forms import LocationForm
from django.shortcuts import render, redirect
from .models import Branch,applicationform


# Create your views here.
def home(request):
    return render(request,'index.html')

def profile(request):
    return render(request,"dashboard.html")

def application(request):
    try:
        if request.method == "POST":
            form = LocationForm(request.POST)
            firstname = request.POST.get('fname')
            lastname = request.POST.get('lname')
            name=firstname+" "+lastname
            dob=request.POST.get('date')
            age=request.POST.get('age')
            gender=request.POST.get('gender')
            phone=request.POST.get('phone')
            mail=request.POST.get('mail')
            addr=request.POST.get('addr')
            acc=request.POST.get('account')
            req = request.POST.getlist('materials')
            if form.is_valid():
                district=form.cleaned_data["district"]
                branch=form.cleaned_data["branch"]
            else:
                print(form.errors)
            if dob != "" and gender != "":
                if applicationform.objects.filter(mail_id=mail).exists():
                    messages.info(request,'Email already Taken')
                    code = 0
                else:
                    submit=applicationform(name=name,Date_of_Birth=dob,age=age,gender=gender,
                                           mail_id=mail,address=addr,phone=phone,district=district,branch=branch,account_ype=acc,materials_to_provide=req)
                    submit.save()
                    code = 1
                    messages.info(request,'Application Submitted Successfully Redirect to')
            else:
                messages.info(request,'Please fill all the details')
                code = 0
                return render(request, 'application.html', {"form": form,"code":code})

        else:
            form = LocationForm()
        return render(request, 'application.html', {"form": form})

    except:

        return render(request, 'application.html', {"form": form})

def load_cities(request):
    district_id = request.GET.get("district")
    branch = Branch.objects.filter(district_id=district_id)
    return render(request, "city_options.html", {"branches": branch})
