from django.db import models

# Create your models here.

class Login(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)

class Camp(models.Model):
    camp_name=models.CharField(max_length=100)
    full_address=models.CharField(max_length=150)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    panchayath=models.CharField(max_length=100)
    thaluk=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)

class Police(models.Model):
    station_id=models.CharField(max_length=100)
    address_line_1=models.CharField(max_length=200)
    address_line_2=models.CharField(max_length=200)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)

class Public(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    panchayath=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)

class Volunteer(models.Model):
    volunteer_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    date_of_birth=models.CharField(max_length=30)
    aadhar_no=models.CharField(max_length=25)
    contact=models.CharField(max_length=15)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    allocation=models.CharField(max_length=100,null=True,blank=True)

class CampUser(models.Model):
    photo=models.ImageField(upload_to='camp')          # Here camp is the folder name where the images added will be stored 
    full_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)
    aadhar_no=models.CharField(max_length=100)
    panchayath=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    thaluk=models.CharField(max_length=100)
    current_date=models.DateField(auto_now_add=True)
    camp_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)

class CampNeeds(models.Model):
    needs=models.TextField(max_length=100)
    status=models.CharField(max_length=100,null=True,blank=True)
    camp_id=models.ForeignKey(Camp,on_delete=models.CASCADE,null=True,blank=True)
    current_date=models.DateField(auto_now_add=True)

class CampAlert(models.Model):
    emergency_message=models.TextField(max_length=50)
    current_date=models.DateField(auto_now_add=True)
    login_id=models.ForeignKey(Camp,on_delete=models.CASCADE,null=True,blank=True)

class VolunteerRequest(models.Model):
    no_of_volunteers=models.CharField(max_length=100)      #   join this table with camp table to alert the volunteers telling  which camp they are allocated to
    volunteer_details=models.TextField(max_length=100)
    current_date=models.DateField(auto_now_add=True)
    login_id=models.ForeignKey(Camp,on_delete=models.CASCADE,null=True,blank=True)

class Allocate(models.Model):
    camp=models.ForeignKey(Camp,on_delete=models.CASCADE,null=True,blank=True) 
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE,null=True,blank=True)
    curr_date=models.DateField(auto_now_add=True)