from django.shortcuts import render
from .forms import CampForm,LoginForm,PoliceForm, PublicForm, VolunteerForm
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

def ViewTables(request):
    users=Login.objects.all()
    camps=Camp.objects.all()
    stations=Police.objects.all()
    publics=Public.objects.all()
    volunteers=Volunteer.objects.all()
    return render(request,'datatable.html',{'users':users,
                  'camps':camps,'statons':stations,'publics':publics,
                  'volunteers':volunteers})

