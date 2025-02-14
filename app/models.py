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
    allocation=models.CharField(max_length=100,null=True,blank=True)      #       Can also set the default as "false".
    

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
    no_of_volunteers=models.IntegerField(default=0)      #   join this table with camp table to alert the volunteers telling  which camp they are allocated to
    totalallocated=models.IntegerField(default=0)
    volunteer_details=models.TextField(max_length=100)
    current_date=models.DateField(auto_now_add=True)
    login_id=models.ForeignKey(Camp,on_delete=models.CASCADE,null=True,blank=True)

class Allocate(models.Model):
    camp=models.ForeignKey(Camp,on_delete=models.CASCADE,null=True,blank=True) 
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE,null=True,blank=True)
    curr_date=models.DateField(auto_now_add=True)
    duty_status=models.CharField(max_length=100,default="Not Scheduled") #   To be not able to schedule volunteers who have already been scheduled to a camp.

class Complaint(models.Model):
    complaint_sub=models.CharField(max_length=100)
    complaint=models.TextField(max_length=500)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    current_date=models.DateField(auto_now_add=True)
    reply=models.TextField(max_length=500,null=True,blank=True)

class Duty(models.Model):
    duty=models.TextField()
    curr_date=models.DateField(auto_now_add=True)
    volunteer_id=models.ForeignKey(Volunteer,on_delete=models.CASCADE,null=True,blank=True)
    camp_id=models.ForeignKey(Camp,on_delete=models.CASCADE,null=True,blank=True)

class FundAllocationModel(models.Model):
    image=models.ImageField(upload_to='fund')
    full_name=models.CharField(max_length=100)
    full_address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    panchayath=models.CharField(max_length=100)
    ration_card_no=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    other_details=models.TextField(max_length=100)
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    current_date=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=0)

class FundPayment(models.Model):
    name_on_card=models.CharField(max_length=100)
    card_no=models.IntegerField(default=0)
    expiring_date=models.CharField(max_length=10)
    cvv_no=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    current_date=models.DateField(auto_now_add=True)
    req_id=models.ForeignKey(FundAllocationModel,on_delete=models.CASCADE,null=True,blank=True)