from django.urls import path
from . import views

urlpatterns = [
    path("camp_reg/", views.CampReg, name="CampReg"),
    path("police_reg/",views.PoliceReg, name="PoliceReg"),
    path("public_reg/",views.PublicReg,name="PublicReg"),
    path("volunteer_reg/", views.VolunteerReg, name="VolunteerReg"),
   # path("view_admin/",views.ViewAdmin,name="ViewAdmin"),
    path("camp_tables/",views.CampTable, name="CampTable"),
    path("station_tables/",views.StationTable, name="StationTable"),
    path("public_tables/",views.PublicTable, name="PublicTable"),
    path("volunteer_tables/",views.VolunteerTable, name="VolunteerTable"),
    path("login/",views.UserLogin,name="UserLogin"),
    path("campHome/",views.CampHome, name='CampHome'),
    path("stationHome/",views.StationHome, name='StationHome'),
    path("publicHome/",views.PublicHome, name='PublicHome'),
    path("volunteerHome/",views.VolunteerHome, name='VolunteerHome'),
    path("editcamp/",views.EditCamp, name='EditCamp'),
    path("editstation/",views.EditStation, name='EditStation'),
    path("editpublic/",views.EditPublic, name='EditPublic'),
    path("editvolunteer/",views.EditVolunteer, name='EditVolunteer'),
    path('admin_view/',views.ViewAdmin2,name='ViewAdmin2'),
    path('camp_user_reg',views.CampAddUser,name="CampAddUser"),
    path('campusersview',views.CampUsersView,name="CampUsersView")
]
