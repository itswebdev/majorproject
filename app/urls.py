from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path( '',views.Landing,name="Landing"),

    path("camp_reg/", views.CampReg, name="CampReg"),
    path("police_reg/",views.PoliceReg, name="PoliceReg"),
    path("public_reg/",views.PublicReg,name="PublicReg"),
    path("volunteer_reg/", views.VolunteerReg, name="VolunteerReg"),
   # path("view_admin/",views.ViewAdmin,name="ViewAdmin"),

    path("camp_tables/",views.CampTable, name="CampTable"),
    path("station_tables/",views.StationTable, name="StationTable"),
    path("public_tables/",views.PublicTable, name="PublicTable"),
    path("volunteer_tables/",views.VolunteerTable, name="VolunteerTable"),
    path("camp_needs_table/",views.CampNeedsTable, name="CampNeedsTable"),

    path("login/",views.UserLogin,name="UserLogin"),
    path("logout/",views.Logout,name="Logout"),

    path("campHome/",views.CampHome, name='CampHome'),
    path("stationHome/",views.StationHome, name='StationHome'),
    path("publicHome/",views.PublicHome, name='PublicHome'),
    path("volunteerHome/",views.VolunteerHome, name='VolunteerHome'),

    path("editcamp/",views.EditCamp, name='EditCamp'),                             
    path("editstation/",views.EditStation, name='EditStation'),
    path("editpublic/",views.EditPublic, name='EditPublic'),
    path("editvolunteer/",views.EditVolunteer, name='EditVolunteer'),

    path('admin_view/',views.ViewAdmin2,name='ViewAdmin2'),

    path('camp_user_reg',views.CampAddUser,name="CampAddUser"),                     #         path of adding camp user
    path('campusersview',views.CampUsersView,name="CampUsersView"),                 #         path of viewing camp user
    path('camp_user_edit/<int:id>',views.EditCampUser,name="EditCampUser"),         #         path of editing camp user
    path('camp_user_delete/<int:id>/',views.CampUserDelete,name="CampUserDelete"),  #         path of deleting camp user

    path('camp_search',views.CampSearch,name="CampSearch"),

    path('camp_needs',views.CampNeedsSubmit,name="CampNeedsSubmit"),
    path('needs_view',views.NeedsViewTable,name="NeedsViewTable"),
    path('edit_camp_need/<int:id>',views.EditCampNeed,name="EditCampNeed"),
    path('delete_camp_need/<int:id>/',views.CampNeedsDelete,name="DeleteCampNeed"),
    path('set_camp_need_status/<int:id>',views.SetCampNeedStatus,name="SetCampNeedStatus"),

    path('camp_person_search',views.SearchCampPerson,name="SearchCampPerson"),
    path('person_search',views.SearchPerson,name="SearchPerson"),

    path('camp_alert',views.CampAlerts,name="CampAlerts"),
    path('camp_alert_table',views.CampAlertTable,name="CampAlertTable"),
    path('alert_table',views.AlertCampTable,name="AlertCampTable"), 
    path('delete_alert/<int:id>',views.DeleteAlert,name="DeleteAlert"), 
    
    #       Request for volunteers required by camp

    path('volunteer_req',views.VolunteerReq,name="VolunteerReq"),
    path('volunteer_req_table',views.VolunteerReqTable,name="VolunteerReqTable"),
    path('req_volunteer_table',views.ReqVolunteerTable,name="ReqVolunteerTable"),
    path('edit_volunteer_req/<int:id>',views.EditVolunteerReq,name="EditVolunteerReq"),
    path('delete_volunteer_req/<int:id>',views.DeleteVolunteerReq,name="DeleteVolunteerReq"),

    path('volunteer_allocate_table/<int:id>/<int:requestid>',views.VolunteerAllocateTable,name="VolunteerAllocateTable"),
    path('VolAllocateNow/<int:campid>/<int:id>/<int:volreqid>',views.VolAllocateNow,name="VolAllocateNow"),
    path('VolDeAllocate/<int:campid>/<int:id>/<int:volreqid>',views.VolDeAllocate,name="VolDeAllocate"),
    
    path('Notification',views.Notification,name="Notification"),

    path('PublicComplaint',views.PublicComplaint,name="PublicComplaint"),
    path('ViewComplaints',views.ViewComplaints,name="ViewComplaints"),
    path('ListComplaints',views.ListComplaints,name="ListComplaints"),
    path('EditComplaint/<int:id>',views.EditComplaint,name="EditComplaint"),
    path('DeleteComplaint/<int:id>',views.DeleteComplaint,name="DeleteComplaint"),
    path('allocated_vol_List',views.AllocatedVolList,name="AllocatedVolList"),            #    List of the volunteers assingned to the camp
    path('ScheduleDuty/<int:camp>/<int:volunteer>',views.ScheduleDuty,name="ScheduleDuty"),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # new 
 