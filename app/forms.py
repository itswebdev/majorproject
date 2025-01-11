from django import forms
from .models import Camp, Login, Police, Public, Volunteer

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

