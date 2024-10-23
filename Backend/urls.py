from django.urls import path
from Backend import views


urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('addcountry/', views.addcountry, name="addcountry"),
    path('save_addcountry/', views.save_addcountry, name="save_addcountry"),
    path('dis_addcountry/', views.dis_addcountry, name="dis_addcountry"),
    path('edit_country/<int:dataid>/', views.edit_country, name="edit_country"),
    path('update_country/<int:dataid>/', views.update_country, name="update_country"),
    path('delete_country/<int:dataid>/', views.delete_country, name="delete_country"),


    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),


    path('addplace/', views.addplace, name="addplace"),
    path('save_place/', views.save_place, name="save_place"),
    path('dis_place/', views.dis_place, name="dis_place"),
    path('edit_place/<int:dataid>/', views.edit_place, name="edit_place"),
    path('update_place/<int:dataid>/', views.update_place, name="update_place"),
    path('delete_place/<int:dataid>/', views.delete_place, name="delete_place"),


    path('addspecial_offer/', views.addspecial_offer, name="addspecial_offer"),
    path('save_offer/', views.save_offer, name="save_offer"),
    path('dis_offers/', views.dis_offers, name="dis_offers"),
    path('edit_offers/<int:dataid>/', views.edit_offers, name="edit_offers"),
    path('update_offer/<int:dataid>/', views.update_offer, name="update_offer"),
    path('delete_offers/<int:dataid>/', views.delete_offers, name="delete_offers"),


    path('addpackages/', views.addpackages, name="addpackages"),
    path('save_package/', views.save_package, name="save_package"),
    path('dis_package/', views.dis_package, name="dis_package"),
    path('edit_package/<int:dataid>/', views.edit_package, name="edit_package"),
    path('update_package/<int:dataid>/', views.update_package, name="update_package"),
    path('delete_package/<int:dataid>/', views.delete_package, name="delete_package"),


    path('add_place_details/', views.add_place_details, name="add_place_details"),
    path('save_place_details/', views.save_place_details, name="save_place_details"),
    path('dis_pdetails/', views.dis_pdetails, name="dis_pdetails"),
    path('edit_pdetails/<int:dataid>/', views.edit_pdetails, name="edit_pdetails"),
    path('update_pdetails/<int:dataid>/', views.update_pdetails, name="update_pdetails"),
    path('delete_pdetails/<int:dataid>/', views.delete_pdetails, name="delete_pdetails"),


    path('add_hotel/', views.add_hotel, name="add_hotel"),
    path('save_Hotel/', views.save_Hotel, name="save_Hotel"),
    path('dis_hotel/', views.dis_hotel, name="dis_hotel"),
    path('edit_hotel/<int:dataid>/', views.edit_hotel, name="edit_hotel"),
    path('update_hotel/<int:dataid>/', views.update_hotel, name="update_hotel"),
    path('delete_hotel/<int:dataid>/', views.delete_hotel, name="delete_hotel"),


    path('addflight/', views.addflight, name="addflight"),
    path('save_addflight/', views.save_addflight, name="save_addflight"),
    path('flight_detail/', views.flight_detail, name="flight_detail"),


    path('contact_details/', views.contact_details, name="contact_details"),
    path('delete_contact_details/<int:dataid>/', views.delete_contact_details, name="delete_contact_details"),
]