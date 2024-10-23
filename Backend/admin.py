from django.contrib import admin
from Backend.models import country_db,hotel_db,flight_db,placeDetails_db,place_db,package_db,offer_db
from Frontend.models import sub_payment

# Register your models here.
admin.site.register(country_db),
admin.site.register(hotel_db),
admin.site.register(flight_db),
admin.site.register(package_db),
admin.site.register(place_db),
admin.site.register(placeDetails_db),
admin.site.register(offer_db),

admin.site.register(sub_payment)