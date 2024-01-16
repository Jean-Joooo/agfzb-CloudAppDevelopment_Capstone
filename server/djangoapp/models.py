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

        def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment):
            # Dealership id
            self.dealership = dealership
            # Reviewer name
            self.name = name
            # Reviewer purchase date
            self.purchase = purchase
            # Review text
            self.review = review
            # Reviewer purchase date
            self.purchase_date = purchase_date
            # Car Make
            self.car_make = car_make
            # Car Model
            self.car_model = car_model
            # Car Year
            self.car_year = car_year
            # Sentiment
            self.sentiment = sentiment

        def __str__(self):
            return "Review: " + self.review
    
        
class ReviewPost:

        def __init__(self, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year):
            # Reviewer name
            self.name = name
            # Dealership id
            self.dealership = dealership
            # Review text
            self.review = review
            # Reviewer purchase date
            self.purchase = purchase
            # Reviewer purchase date
            self.purchase_date = purchase_date
            # Car Make
            self.car_make = car_make
            # Car Model
            self.car_model = car_model
            # Car Year
            self.car_year = car_year

        
        def to_json(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4)   