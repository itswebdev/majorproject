from django.shortcuts import render, redirect, get_object_or_404
from .forms import CampForm,LoginForm,PoliceForm, PublicForm, VolunteerForm, LoginCheck,LoginEditForm,CampUserForm,CampNeedsForm
from django.contrib import messages
from .models import Camp,Login,Police,Volunteer,Public,CampUser,CampNeeds
from django.db.models import Q


# Create your views here.

    # camp Registration form

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
            return redirect('UserLogin')
    else:

        form=CampForm()
        login=LoginForm()
    return render(request, 'registration.html',{'form':form,'login':login})

    # station Registration form

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
            return redirect('UserLogin')
    else:

        form=PoliceForm()
        login=LoginForm()
    return render(request,'registration.html',{'form':form,'login':login})

    # public Registration form

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
            return redirect('UserLogin')
    else:

        form=PublicForm()
        login=LoginForm()
    return render(request, 'registration.html',{'form':form,'login':login})

    # volunteer Registration form

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
            return redirect('UserLogin')
    else:
        form=VolunteerForm()
        login=LoginForm()
    return render(request,'registration.html',{'form':form,'login':login})

# admin home page

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

    # camp home page

def CampHome(request):
    return render(request,'camp.html')

    # station home page

def StationHome(request):
    return render(request,'station.html')

    # public home page

def PublicHome(request):
    return render(request,'public.html')

    
    # volunteer home page

def VolunteerHome(request):
    return render(request,'volunteer.html')


    # user login 

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
                        request.session['camp_id']=user.id
                        return redirect('CampHome')
                    elif user.usertype=="police_station":
                        request.session['station_id']=user.id
                        return redirect('StationHome')
                    elif user.usertype=="public_user":
                        request.session['public_id']=user.id
                        return redirect('PublicHome')
                    elif user.usertype=="volunteer":
                        request.session['volunteer_id']=user.id
                        return redirect('VolunteerHome')    
                else:
                    messages.error(request,"invalid password")
            except Login.DoesNotExist:
                    messages.error(request,"User Does not Exist")
    else:
        form=LoginCheck()
    return render(request,'login.html',{'form':form})


     # camp profile editing

def EditCamp(request):
    id=request.session['camp_id']
    user=get_object_or_404(Login, id=id)
    camp=get_object_or_404(Camp, login_id=user)
    if request.method == "POST":
        login=LoginEditForm(request.POST, instance=user)
        form=CampForm(request.POST, instance=camp)
        if form.is_valid() and login.is_valid():
            form.save()
            login.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('CampHome')
    else:
        login=LoginEditForm(instance=user)
        form=CampForm(instance=camp)
    return render(request,'edit_profile.html',{'form':form,'login':login})

    
     # station profile editing

def EditStation(request):
    id=request.session['station_id']                   
    user=get_object_or_404(Login, id=id)
    station=get_object_or_404(Police, login_id=user)
    if request.method=="POST":
            login=LoginEditForm(request.POST, instance=user)
            form=PoliceForm(request.POST, instance=station)
            if form.is_valid() and login.is_valid():
             form.save()
             login.save()
             messages.success(request,"Profile Updated Successfully")
             return redirect('StationHome')
    else:
      login=LoginEditForm(instance=user)
      form=PoliceForm(instance=station)
    return render(request,'edit_profile.html',{'form':form,'login':login})


     # public profile editing

def EditPublic(request): 
    id=request.session['public_id']
    user=get_object_or_404(Login, id=id)
    public=get_object_or_404(Public, login_id=user)
    if request.method=="POST":
            login=LoginEditForm(request.POST, instance=user)
            form=PublicForm(request.POST, instance=public)
            if form.is_valid() and login.is_valid():
             form.save()
             login.save()
             messages.success(request,"Profile Updated Successfully")
             return redirect('PublicHome')
    else:
      login=LoginEditForm(instance=user)
      form=PublicForm(instance=public)
    return render(request,'edit_profile.html',{'form':form,'login':login})

    # volunteer profile editing

def EditVolunteer(request):                             
    id=request.session['volunteer_id']
    user=get_object_or_404(Login, id=id)
    volunteer=get_object_or_404(Volunteer, login_id=user)
    if request.method=="POST":
            login=LoginEditForm(request.POST, instance=user)
            form=VolunteerForm(request.POST, instance=volunteer)
            if form.is_valid() and login.is_valid():
             form.save()
             login.save()
             messages.success(request,"Profile Updated Successfully")
             return redirect('VolunteerHome')
    else:
      login=LoginEditForm(instance=user)
      form=VolunteerForm(instance=volunteer)
    return render(request,'edit_profile.html',{'form':form,'login':login})

    # admin page view 2

def ViewAdmin2(request):
    return render(request,'admin2.html')

    #  Camp User Registration  

def CampAddUser(request):
    id=request.session['camp_id']                        # We can also use ' id=request.session.get('camp_id') ' instead of this line.
    campdata=get_object_or_404(Login,id=id)
    if request.method=="POST":
        form=CampUserForm(request.POST,request.FILES)    # 'request.FILES' is used because image files are also stored here.
        if form.is_valid():
            camp_user=form.save(commit=False)
            camp_user.camp_id=campdata
            camp_user.save()
            messages.success(request,"Registered Successfully")
            return redirect('CampHome')
    else:

        form=CampUserForm()
    return render(request,'camp_user_reg.html',{'form':form})

    # Camp user viewing

def CampUsersView(request):
    session_id=request.session['camp_id']
    a=get_object_or_404(Login,id=session_id)
    users=CampUser.objects.filter(camp_id=a)
    return render(request,'camp_users_table.html',{'users':users})

    # Editing camp user

def EditCampUser(request,id):
    user=get_object_or_404(CampUser, id=id)
    if request.method=="POST":
        form=CampUserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('CampUsersView') 
    else:
        form=CampUserForm(instance=user)
    return render(request,'edit_camp_user.html',{'form':form})

    # Deleting camp user
 
def CampUserDelete(request,id):
    user=get_object_or_404(CampUser, id=id)
    user.delete()
    messages.success(request,"Deleted Successfully")
    return redirect('CampUsersView')

def Landing(request):
    return render(request,'landing.html')
   
# def CampSearch(request):
#     if request.method=="POST":
#         query=request.POST.get('search')
#         camps=Camp.objects.filter(camp_name__icontains=query,city__icontains=query)
#         return render(request,'camp_search.html',{'camps':camps})
#     else:
#         return render(request,'camp_search.html')
    

    # searching for camps

def CampSearch(request):
    if request.method == "POST":
        query = request.POST.get('search')
        camps = Camp.objects.filter(
            Q(camp_name__icontains=query) |
            Q(district__icontains=query) |
            Q(full_address__icontains=query) |
            Q(city__icontains=query) |
            Q(panchayath__icontains=query) |
            Q(thaluk__icontains=query) |
            Q(contact__icontains=query) 
        )
        return render(request, 'camp_search.html', {'camps': camps})
    else:
        return render(request, 'camp_search.html')


def CampNeedsSubmit(request):
    id=request.session['camp_id']    
    campdata=get_object_or_404(Camp,login_id=id)
    if request.method =="POST":
        form=CampNeedsForm(request.POST)
        if form.is_valid():
            camp_need=form.save(commit=False)
            camp_need.camp_id=campdata
            camp_need.save()
            messages.success(request,"Needs are submitted successfully")
    else:
        form=CampNeedsForm()
    return render(request,'camp_needs.html',{'form':form})

def CampNeedsTable(request):
    needs=CampNeeds.objects.all()
    return render(request,'camp_needs_table.html',{'needs':needs})

def NeedsViewTable(request):
        session_id=request.session['camp_id']
        a=get_object_or_404(Camp,login_id=session_id)
        needs=CampNeeds.objects.filter(camp_id=a)
        return render(request,'needs_view_table.html',{'needs':needs})

def EditCampNeed(request,id):
    need=get_object_or_404(CampNeeds,id=id)
    if request.method=="POST":
        form=CampNeedsForm(request.POST,instance=need)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('NeedsViewTable')
    else:
        form=CampNeedsForm(instance=need)
    return render(request,'camp_needs.html',{'form':form})

def CampNeedsDelete(request,id):
    need=get_object_or_404(CampNeeds,id=id)
    need.delete()
    messages.success(request,"Deleted Successfully")
    return redirect('NeedsViewTable')


   # function to logout

def Logout(request):
    request.session.flush()
    return redirect('Landing')

def SetCampNeedStatus(request,id):
    need=get_object_or_404(CampNeeds,id=id)
    if request.method=="POST":
        need.status=request.POST.get('status')
        need.save()
        messages.success(request,"Status Updated Successfully")
        return redirect('CampNeedsTable')
    else:
        form=CampNeedsForm(instance=need)
    return render(request,'set_camp_status.html',{'form':form})

def SearchCampPerson(request):
    id = request.session['camp_id']
    a=get_object_or_404(Camp,login_id=id)
    if request.method=="POST":
        query=request.POST.get('search')
        users=CampUser.objects.filter(
            Q(camp_id=a) &
            Q(full_name__icontains=query) | 
            Q(address__icontains=query) | 
            Q(district__icontains=query) | 
            Q(city__icontains=query)| 
            Q(contact_no__icontains=query) | 
            Q(aadhar_no__icontains=query) |
            Q(panchayath__icontains=query) | 
            Q(village__icontains=query) |
            Q(thaluk__icontains=query) 
            )      
        return render(request,'camp_search_person.html',{'users':users})