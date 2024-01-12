from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name=models.CharField(null=False, max_length=30, default='CarMake')
    description=models.CharField(max_length=1000)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

class CarModel(models.Model):
    carmake=models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name=models.CharField(null=False, max_length=30, default='CarModel')
    dealerid=models.IntegerField(default=2)
    cartype=models.CharField(max_length=30)
    year=models.DateField(default=now)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Dealer ID: " + str(self.dealer_id) + "," + \
               "Car Type: " + self.car_type + "," + \
               "Year: " + str(self.year) + "," + \
               "Car Make: " + str(self.car_make)

class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
