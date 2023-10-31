from django.db import models
class User(models.Model):
  
    username = models.CharField(max_length=100,default='')
    date = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    phoneno = models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=15,default='')
    fireid = models.CharField(max_length=100,default='')
    profilephoto = models.FileField(upload_to='userProfilePhotos/', null=True, blank=True)
    
    def __str__(self):
        return self.username


class ParkingSpot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    distance = models.CharField(max_length=20)
    time = models.CharField(max_length=30)
    valet = models.CharField(max_length=100)
    description = models.CharField(max_length =1500)
    rate = models.IntegerField() 
    displayphoto = models.FileField(upload_to='displayPhotos/', null=True, blank=True)   
    
    # def __str__(self):
    #     return self.name
    
    
class Vehicle(models.Model):
    modelname = models.CharField(max_length=100)
    platenum = models.CharField(max_length=100)
    fireid = models.CharField(max_length=100,default='')
    # customer = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    
    def __str__(self):
        return self.modelname
    
    
class ParkingDetails(models.Model):
    fireid = models.CharField(max_length=100,default='')
    todaydate  = models.CharField(max_length=100,default='')
    username = models.CharField(max_length=100,default='')
    phoneno = models.CharField(max_length=100,default='')
    vehiclename = models.CharField(max_length=100,default='')
    vehiclenum = models.CharField(max_length=100,default='')
    parkingname = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    selecteddate = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    starthour = models.CharField(max_length=100)
    endhour = models.CharField(max_length=100)
    totalcost = models.CharField(max_length=100,default='')
    floornum = models.CharField(max_length=100,default='')
    spotnum = models.CharField(max_length=100,default='')
    displayphoto = models.CharField(max_length=100,default='')
    
    # def __str__(self):
    #     return self.fireid
    

class Ewallet(models.Model):
    email = models.CharField(max_length=100,default='')
    # useridval = models.CharField(max_length=100,default='')
    fireid = models.CharField(max_length=100)
    balance = models.CharField(max_length=100,default='0')
    
    
class SavedParkinglot(models.Model):
    fireid = models.CharField(max_length=100)
    spotname = models.CharField(max_length=100)
    spotaddress = models.CharField(max_length=100)
    displayphoto = models.CharField(max_length=100,default='')
    parkid = models.CharField(max_length=100,default='')