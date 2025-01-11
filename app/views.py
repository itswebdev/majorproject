from django.shortcuts import render, redirect
from .forms import CampForm,LoginForm,PoliceForm, PublicForm, VolunteerForm, LoginCheck
from django.contrib import messages
from .models import Camp,Login,Police,Volunteer,Public

# Create your views here.

def CampReg(request):
    if request.method=="POST":
        form=CampForm(request.POST)
        login=LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user=login.save(commit=False)
            user.usertype='camp'
            user.save()
            a=form.save(commit=False)
            a.login_id=user
            a.save()
            messages.success(request,"Camp Registered Successfully")
    else:

        form=CampForm()
        login=LoginForm()
    return render(request, 'camp_reg.html',{'form':form,'login':login})

def PoliceReg(request):
    if request.method=="POST":
        form=PoliceForm(request.POST)
        login=LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user=login.save(commit=False)
            user.usertype='police_station'
            user.save()
            station=form.save(commit=False)
            station.login_id=user
            station.save()
            messages.success(request,"Police Station Registered Successfully")
    else:

        form=PoliceForm()
        login=LoginForm()
    return render(request,'police_reg.html',{'form':form,'login':login})

def PublicReg(request):
    if request.method=="POST":
        form=PublicForm(request.POST)
        login=LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user=login.save(commit=False)
            user.usertype='public_user'
            user.save()
            a=form.save(commit=False)
            a.login_id=user
            a.save()
            messages.success(request,"User Registration Successfully")
    else:

        form=PublicForm()
        login=LoginForm()
    return render(request, 'public_reg.html',{'form':form,'login':login})

def VolunteerReg(request):
    if request.method=="POST":
        form=VolunteerForm(request.POST)
        login=LoginForm(request.POST)
        if form.is_valid() and login.is_valid():
            user=login.save(commit=False)
            user.usertype='volunteer'
            user.save()
            a=form.save(commit=False)
            a.login_id=user
            a.save()
            messages.success(request,"Volunteer Registered successfully")
    else:
        form=VolunteerForm()
        login=LoginForm()
    return render(request,'volunteer_reg.html',{'form':form,'login':login})

def ViewAdmin(request):
    return render(request,'admin.html')

def CampTable(request):
    camps=Camp.objects.all()
    return render(request,'camp_table.html',{'camps':camps})

def StationTable(request):
     stations=Police.objects.all()
     return render(request,'station_table.html',{'stations':stations})

def PublicTable(request):
    publics=Public.objects.all()
    return render(request,'public_table.html',{'publics':publics})

def VolunteerTable(request):
    volunteers=Volunteer.objects.all()
    return render(request,'volunteer_table.html',{'volunteers':volunteers})

def Camp(request):
    return render(request,'camp.html')

def Station(request):
    return render(request,'station.html')

def Public(request):
    return render(request,'public.html')

def Volunteer(request):
    return render(request,'volunteer.html')


def UserLogin(request):
    if request.method=="POST":
        form=LoginCheck(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                user=Login.objects.get(email=email)
                if user.password==password:
                    if user.usertype=="camp":
                        return render(request,'camp.html')
                    elif user.usertype=="police_station":
                        return render(request,'station.html')
                    elif user.usertype=="public_user":
                        return render(request,'public.html')
                    elif user.usertype=="volunteer":
                        return render(request,'volunteer.html')    
                else:
                    messages.error(request,"invalid password")
            except Login.DoesNotExist:
                    messages.error(request,"User Does not Exist")
    else:
        form=LoginCheck()
    return render(request,'login.html',{'form':form})


