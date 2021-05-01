# Path function is necessary for adding urls
from django.urls import path
from django.contrib.auth.models import User


# Imports everything form views
from . import views

app_name = 'pizzas'

# A list of individual pages' urls
urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas',views.pies, name='pizzas'),
    path('new_pizza/',views.new_pizza, name='new_pizza'),
    path('new_topping/' ,views.new_topping, name='new_topping'),
    path('pizzas/<int:pizza_id>/',views.pies, name='pizzas'), 


]

