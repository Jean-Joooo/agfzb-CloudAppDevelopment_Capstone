from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.

class CarMake(models.Model):
    name=models.CharField(null=False, max_length=30, default='Car Name')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    id = models.IntegerField(default=1,primary_key=True)

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    SPORT = "Sport"
    COUPE = "Coupe"
    OTHER = "Other"
    CAR_CHOICES = [(SEDAN, "Sedan"), (SUV, "SUV"), (WAGON, "Station wagon"), (SPORT, "Sports Car"),
                   (COUPE, "Coupe"), (OTHER, 'Other')]

    model_type = models.CharField(null=False, max_length=15, choices=CAR_CHOICES, default=SEDAN)

    YEAR_CHOICES = []
    for r in range(1980, datetime.datetime.now().year):
        YEAR_CHOICES.append((r, r))

    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return self.name + ", " + str(self.year) + ", " + self.model_ty

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