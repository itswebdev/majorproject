from django import forms
from .models import Camp, Login, Police, Public, Volunteer, CampUser,CampNeeds,CampAlert,VolunteerRequest,Complaint

class CampForm(forms.ModelForm):
    
    class Meta:
        model=Camp
        fields=['camp_name','full_address','district','city','panchayath','thaluk','contact']

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']

class PoliceForm(forms.ModelForm):
    class Meta:
        model=Police
        fields=['station_id','address_line_1','address_line_2','district','city','contact']

class PublicForm(forms.ModelForm):
    class Meta:
        model=Public
        fields=['fullname','address','pincode','district','city','panchayath','village','contact']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model=Volunteer
        fields=['volunteer_name','gender','date_of_birth','aadhar_no','contact']

class LoginCheck(forms.Form):
    email=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class LoginEditForm(forms.ModelForm): # form for profile editing
    class Meta:
        model=Login
        fields=['email']


class CampUserForm(forms.ModelForm):
    class Meta:
        model=CampUser
        fields=['photo','full_name','address','district','city','contact_no','aadhar_no','panchayath','village','thaluk']

class CampNeedsForm(forms.ModelForm):
    class Meta:
        model=CampNeeds
        fields=['needs'] 

class CampAlertForm(forms.ModelForm):
    class Meta:
        model=CampAlert
        fields=['emergency_message']

class VolunteerReqForm(forms.ModelForm):
    class Meta:
        model=VolunteerRequest
        fields=['no_of_volunteers','volunteer_details']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=['complaint_sub','complaint']