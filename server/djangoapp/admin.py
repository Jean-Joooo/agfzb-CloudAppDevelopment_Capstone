from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name', 'description']

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealer_id', 'car_type', 'year')
    list_filter = ['name']
    search_fields = ['name', 'dealer_id', 'car_type', 'year']

admin.site.register(CarModel)
admin.site.register(CarMake)

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
