from django.db import models

# Create your models here.
class country_db(models.Model):
    Country = models.CharField(max_length=25,null=True,blank=True)
    Image = models.ImageField(upload_to="Cimage",null=True,blank=True)
    No_tour_place = models.CharField(max_length=50,null=True,blank=True)

class place_db(models.Model):
    Country = models.CharField(max_length=25,null=True,blank=True)
    Name = models.CharField(max_length=25,null=True,blank=True)
    Place = models.CharField(max_length=35,null=True,blank=True)
    Image = models.ImageField(upload_to="pimg",null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)


class offer_db(models.Model):
    Country = models.CharField(max_length=30,null=True,blank=True)
    Place = models.CharField(max_length=30,null=True,blank=True)
    Details = models.CharField(max_length=30,null=True,blank=True)
    Rating = models.CharField(max_length=30,null=True,blank=True)
    Hotel = models.CharField(max_length=30,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    Discount = models.IntegerField(null=True,blank=True)
    Image1 = models.ImageField(upload_to="offers",null=True,blank=True)
    Image2 = models.ImageField(upload_to="offers",null=True,blank=True)
    Image3 = models.ImageField(upload_to="offers",null=True,blank=True)
    Image4 = models.ImageField(upload_to="offers",null=True,blank=True)

class package_db(models.Model):
    Country = models.CharField(max_length=30,null=True,blank=True)
    Place = models.CharField(max_length=30,null=True,blank=True)
    Details = models.CharField(max_length=30,null=True,blank=True)
    Rating = models.CharField(max_length=30,null=True,blank=True)
    Hotel = models.CharField(max_length=30,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    Discount = models.IntegerField(null=True,blank=True)
    Image1 = models.ImageField(upload_to="package",null=True,blank=True)
    Image2 = models.ImageField(upload_to="package",null=True,blank=True)
    Image3 = models.ImageField(upload_to="package",null=True,blank=True)
    Image4 = models.ImageField(upload_to="package",null=True,blank=True)


class placeDetails_db(models.Model):
    Place = models.CharField(max_length=30,null=True,blank=True)
    Country = models.CharField(max_length=30,null=True,blank=True)
    Details = models.CharField(max_length=200,null=True,blank=True)
    Image = models.ImageField(upload_to="PlaceDetails",null=True,blank=True)

class hotel_db(models.Model):
    Country = models.CharField(max_length=30,null=True,blank=True)
    Place = models.CharField(max_length=30,null=True,blank=True)
    Location = models.CharField(max_length=100,null=True,blank=True)
    Details = models.CharField(max_length=30,null=True,blank=True)
    Rating = models.CharField(max_length=30,null=True,blank=True)
    Hotel = models.CharField(max_length=30,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    Discount = models.IntegerField(null=True,blank=True)
    Image1 = models.ImageField(upload_to="package",null=True,blank=True)
    Image2 = models.ImageField(upload_to="package",null=True,blank=True)
    Image3 = models.ImageField(upload_to="package",null=True,blank=True)
    Image4 = models.ImageField(upload_to="package",null=True,blank=True)


class flight_db(models.Model):
    From = models.CharField(max_length=100,null=True,blank=True)
    To = models.CharField(max_length=100,null=True,blank=True)
    From_City = models.CharField(max_length=100,null=True,blank=True)
    From_country = models.CharField(max_length=100,null=True,blank=True)
    To_city = models.CharField(max_length=100,null=True,blank=True)
    To_Country = models.CharField(max_length=100,null=True,blank=True)
    Flight_name = models.CharField(max_length=100,null=True,blank=True)
    Flight_No = models.CharField(max_length=100,null=True,blank=True)
    Depature_time = models.CharField(max_length=100,null=True,blank=True)
    Landing_time = models.CharField(max_length=100,null=True,blank=True)
    Charge = models.CharField(max_length=100,null=True,blank=True)