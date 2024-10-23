from django.urls import path
from Frontend import views


urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('destination/', views.destination, name="destination"),
    path('place/<cname>/', views.place, name="place"),
    path('hotel/', views.hotel, name="hotel"),
    path('placedetails/<pname>/', views.placedetails, name="placedetails"),
    path('select_hotel/<int:dataid>/', views.select_hotel, name="select_hotel"),
    path('hotel_booking/<int:dataid>', views.hotel_booking, name="hotel_booking"),
    path('save_hotelBooking', views.save_hotelBooking, name="save_hotelBooking"),
    path('success/', views.success, name="success"),
    path('blogs/', views.blogs, name="blogs"),
    path('createBlog/', views.createBlog, name="createBlog"),
    path('save_createBlog/', views.save_createBlog, name="save_createBlog"),
    path('blog_details/<int:dataid>', views.blog_details, name="blog_details"),



    path('login_page/', views.login_page, name="login_page"),
    path('register_page/', views.register_page, name="register_page"),
    path('save_register/', views.save_register, name="save_register"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('user_logout/', views.user_logout, name="user_logout"),


    path('subscription/', views.subscription, name="subscription"),
    path('subscription_form/', views.subscription_form, name="subscription_form"),
    path('sub_success/', views.sub_success, name="sub_success"),


    path('flight/', views.flight, name="flight"),
    path('book_flight/<int:dataid>/', views.book_flight, name="book_flight"),



    path('profile/<user>/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('update_profile/', views.update_profile, name="update_profile"),


    path('h_payment/', views.h_payment, name="h_payment"),
    path('rating/', views.rating, name="rating"),
    path('rating_save/', views.rating_save, name="rating_save"),
    path('send_email/', views.send_email, name="send_email"),
    path('flight_email/', views.flight_email, name="flight_email"),


    path('flight_payment/', views.flight_payment, name="flight_payment"),
    path('save_book_flight/', views.save_book_flight, name="save_book_flight"),

    path('contact/', views.contact, name="contact"),
    path('save_contact/', views.save_contact, name="save_contact"),

    path('Offers_booking/', views.Offers_booking, name="Offers_booking"),
    path('offer_details/<int:dataid>/', views.offer_details, name="offer_details"),
    path('package_booking/', views.package_booking, name="package_booking"),



]