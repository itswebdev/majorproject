from django.urls import path
from . import views

urlpatterns = [
    path("camp_reg/", views.CampReg, name="CampReg"),
    path("police_reg/",views.PoliceReg, name="PoliceReg"),
    path("public_reg/",views.PublicReg,name="PublicReg"),
    path("volunteer_reg/", views.VolunteerReg, name="VolunteerReg"),
    path("view_admin/",views.ViewAdmin,name="ViewAdmin"),
    path("camp_tables/",views.CampTable, name="CampTable"),
    path("station_tables/",views.StationTable, name="StationTable"),
    path("public_tables/",views.PublicTable, name="PublicTable"),
    path("volunteer_tables/",views.VolunteerTable, name="VolunteerTable"),
    path("login/",views.UserLogin,name="UserCamp"),
    path("camp/",views.Camp, name='Camp'),
    path("station/",views.Station, name='Station'),
    path("public/",views.Public, name='Public'),
    path("volunteer/",views.Volunteer, name='Volunteer'),
    path("editprofile/<int:id>/",views.EditProfile, name='EditProfile')
]
