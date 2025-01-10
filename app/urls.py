from django.urls import path
from . import views

urlpatterns = [
    path("camp_reg/", views.CampReg, name="CampReg"),
    path("police_reg/",views.PoliceReg, name="PoliceReg"),
    path("public_reg/",views.PublicReg,name="PublicReg"),
    path("volunteer_reg/", views.VolunteerReg, name="VolunteerReg"),
    path("view_admin/",views.ViewAdmin,name="ViewAdmin")
]
