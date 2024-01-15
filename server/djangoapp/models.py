from django.db import models
from django.core import serializers
from django.utils.timezone import now
import uuid
import json
import datetime

# Create your models here.

class CarMake(models.Model):
    name=models.CharField(null=False, max_length=30, default='Car Name')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return "Name: " + self.name

# Car Model model
class CarModel(models.Model):
    id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(null=False, max_length=100, default='Car')
    type = models.CharField(null=False, max_length=100, default='Car Type')
   
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    MINIVAN = 'Minivan'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (MINIVAN, 'Minivan')
    ]

    type = models.CharField(
        null=False,
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN
    )
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name + \
               "type: " + self.type

class CarDealer:

    def __init__(self, address, city, id, lat, long, st, zip, full_name):
        self.address = address
        self.city = city
        self.id = id
        self.lat = lat
        self.long = long
        self.st = st
        self.zip = zip
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name


class DealerReview:
    def __init__(self, dealership, name, purchase,review, purchase_date, car_make, car_model, id):
        self.dealership = dealership
        self.name= name
        self.purchase= purchase
        self.review=review
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.id=id

    def __str__(self):
        return "Dealer review:" +self.review


class ReviewPost:
    def __init__(self, dealership, name, purchase,review, purchase_date, car_make, car_model, id):
        self.dealership = dealership
        self.name= name
        self.purchase= purchase
        self.review=review
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.id=id

    def __str__(self):
        return "Dealer review:" +self.review