from django.contrib import admin

# Register your models here.
from .models import Pizza,Topping
# Resgisters each of the models to the page
admin.site.register(Pizza)
admin.site.register(Topping)
