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
