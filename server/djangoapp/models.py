from django.db import models
from django.core import serializers
from django.utils.timezone import now
import uuid
import json

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='undifined')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class CarModel(models.Model):
        SEDAN = 'sedan'
        SUV = 'suv'
        WAGON = 'wagon'
        CAR_TYPE_CHOICES = [
            (SEDAN, 'Sedan'),
            (SUV, 'SUV'),
            (WAGON, 'Wagon'),
        ]
        make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=30, default='undifined')
        type = models.CharField(null=False, max_length=20, choices= CAR_TYPE_CHOICES, default='SEDAN')
        year = models.DateField(default=now, editable=True)
        
        def __str__(self):
            return self.name

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
    
class DealerReview:

    def __init__(dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        # Dealership id
        self.dealership = dealership
        # Reviewer name
        self.name = name
        # Purchase
        self.purchase = purchase
        # Review
        self.review = review
        # Purchase date
        self.purchase_date = purchase_date
        # Car make
        self.car_make = car_make
        # Car model
        self.car_model = car_model
        # Car year
        self.car_year = car_year
        # Sentiment
        self.sentiment = sentiment
        # id
        self.id = id

    def __str__(self):
        return "Review: " + self.review
    
class ReviewPost:

    def __init__(dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        # Dealership
        self.dealership = dealership
        # Reviewer name
        self.name = name
        # Purchase
        self.purchase = purchase
        # Review
        self.review = review
        # Purchase date
        self.purchase_date = purchase_date
        # Car make
        self.car_make = car_make
        # Car model
        self.car_model = car_model
        # Car year
        self.car_year = car_year
        # Sentiment
        self.sentiment = sentiment
        # id
        self.id = id

    def __str__(self):
        return "review: " + self.review