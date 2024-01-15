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

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'name', 'id', 'model_type', 'year']
    list_filter = ['model_type', 'car_make', 'id', 'year',]
    search_fields = ['car_make', 'name']

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
