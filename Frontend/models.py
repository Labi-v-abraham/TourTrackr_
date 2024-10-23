from django.db import models
from django.contrib.auth.models import AbstractUser
from TourTrackr import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("Date must be in the future.")

class register_db(models.Model):
    Username = models.CharField(max_length=25,null=True,blank=True)
    Email = models.CharField(max_length=55,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=25,null=True,blank=True)
    Place = models.CharField(max_length=30,null=True,blank=True)
    Country = models.CharField(max_length=30,null=True,blank=True)
    Name = models.CharField(max_length=30,null=True,blank=True)


class HotelBooking_db(models.Model):
    Hotel_Name = models.CharField(max_length=50,null=True,blank=True)
    First_Name = models.CharField(max_length=20,null=True,blank=True)
    Last_Name = models.CharField(max_length=20,null=True,blank=True)
    Email_Id = models.CharField(max_length=80,null=True,blank=True)
    Room = models.CharField(max_length=50,null=True,blank=True)
    No_of_people = models.IntegerField(null=True,blank=True)
    Arrive_Date = models.CharField(max_length=50,null=True,blank=True)
    Arrive_Time = models.CharField(max_length=50,null=True,blank=True)
    Time = models.CharField(max_length=20,null=True,blank=True)
    Departure_Month = models.CharField(max_length=30,null=True,blank=True)
    Departure_Day = models.CharField(max_length=30,null=True,blank=True)
    Departure_Year = models.CharField(max_length=30,null=True,blank=True)
    Pick_Up = models.CharField(max_length=40,null=True,blank=True)
    Flight_No = models.CharField(max_length=100,null=True,blank=True)
    Request = models.CharField(max_length=250,null=True,blank=True)



class blog_db(models.Model):
    user = models.CharField(max_length=30,null=True,blank=True)
    date = models.CharField(max_length=30,null=True,blank=True)
    image1 = models.ImageField(upload_to="blogs",null=True,blank=True)
    image2 = models.ImageField(upload_to="blogs",null=True,blank=True)
    title = models.CharField(max_length=70,null=True,blank=True)
    summary = models.CharField(max_length=200,null=True,blank=True)
    detail = models.CharField(max_length=1000,null=True,blank=True)


class hotel_booking_db(models.Model):
    User = models.CharField(max_length=30,null=True,blank=True)
    Hotel_name = models.CharField(max_length=50,null=True,blank=True)
    First_name = models.CharField(max_length=30,null=True,blank=True)
    Second_name = models.CharField(max_length=30,null=True,blank=True)
    Email = models.CharField(max_length=80,null=True,blank=True)
    Room = models.CharField(max_length=80,null=True,blank=True)
    No_of_guest = models.CharField(max_length=30,null=True,blank=True)
    Arrive_date = models.CharField(max_length=30,null=True,blank=True)
    Arrive_time = models.CharField(max_length=30,null=True,blank=True)
    Arrive_apm = models.CharField(max_length=30,null=True,blank=True)
    Checkout = models.CharField(max_length=30,null=True,blank=True)
    Pickup = models.CharField(max_length=30,null=True,blank=True)
    Flight = models.CharField(max_length=40,null=True,blank=True)
    Request = models.CharField(max_length=500,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Bill = models.IntegerField(null=True,blank=True)


class subscription_db(models.Model):
    user = models.CharField(max_length=30,null=True,blank=True)
    email = models.CharField(max_length=80,null=True)
    subscribed = models.BooleanField(default=True)


class sub_payment(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    payment_id = models.CharField(max_length=200,null=True,blank=True)
    paid = models.BooleanField(default=False)

class review_db(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)

class flight_booking_db(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    First_name = models.CharField(max_length=40,null=True,blank=True)
    Second_name = models.CharField(max_length=40,null=True,blank=True)
    Email = models.EmailField(max_length=80,null=True,blank=True)
    Type = models.CharField(max_length=80,null=True,blank=True)
    No_person = models.IntegerField(null=True,blank=True)
    Date = models.DateField(validators=[validate_future_date],null=True,blank=True)
    Flight = models.CharField(max_length=100,null=True,blank=True)
    Flight_no = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Time = models.CharField(max_length=30,null=True,blank=True)


class contact_db(models.Model):
    Name = models.CharField(max_length=40,null=True,blank=True)
    Email = models.EmailField(max_length=80,null=True,blank=True)
    Message = models.CharField(max_length=200,null=True,blank=True)