# Path function is necessary for adding urls
from django.urls import path

# Imports everything form views
from . import views

app_name = "pizzas"

# A list of individual pages' urls
urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id',views.pizzas, name='pizzas'), 
    path('new_pizza/',views.new_pizza, name='new_pizza'),

]

