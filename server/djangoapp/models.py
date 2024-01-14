from django.db import models
from django.utils.timezone import now

# Create your models here.

class CarMake(models.Model):
    name=models.CharField(null=False, max_length=30, default='Car Name')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

class CarModel(models.Model):
    CarMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='CarModel')
    dealerId = models.IntegerField(null=False, default=0)
    year = models.DateField(null=False, default=now)

    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    Sport = 'Sport car'
    OTHER = 'Other'
    CAR_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (Sport, 'Sport car'),
        (OTHER, 'Other'),
    ]

    carType = models.CharField(null=False, max_length=20, choices=CAR_CHOICES, default=OTHER)

    def __str__(self):
        return "Name" + self.name + "," + \
            "Type" + self.carType + "," + \
            "Year" + self.year + "," + \
            "DealerId" + self.dealerId

class DealerReview(models.Model):
    dealership = models.CharField(null=True, max_length=30, default='Dealer Name')
    name = models.CharField(null=True, max_length=30, default='Car Name')
    purchase = models.CharField(null=True, max_length=30, default='Purchase')
    review = models.CharField(null=True, max_length=30, default='Review')
    purchaseDate = models.DateField(null=True, default=now)
    carMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    carModel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    carYear = models.DateField(null=True, default=now)
    sentiment = models.CharField(null=True, max_length=30, default='Sentiment')
    dealerId = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "Dealer name: " + self.full_name

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