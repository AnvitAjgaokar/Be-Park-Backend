from django.contrib import admin
from .models import User, ParkingDetails,ParkingSpot,Vehicle,Ewallet,SavedParkinglot


# Register your models here.
admin.site.register(User)
admin.site.register(ParkingSpot)
admin.site.register(ParkingDetails)
admin.site.register(Vehicle)
admin.site.register(Ewallet)
admin.site.register(SavedParkinglot)


