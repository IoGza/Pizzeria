# Path function is necessary for adding urls
from django.urls import path
from django.contrib.auth.models import User
import pizzas


# Imports everything form views
from . import views

app_name = 'pizzas'
from django.conf.urls.static import static
from pizzeria import settings

# A list of individual pages' urls
urlpatterns = [
    path('', pizzas.views.index, name='index'),
    path('pizzas',views.pies, name='pizzas'),
    # path('pizzas/<int:pizza_id>/',views.pies, name='pizzas'),    
    path('new_pizza/',views.new_pizza, name='new_pizza'),
    path('new_pizza/<int:pizza_id>/',views.new_pizza, name='new_pizza'),
    # path('single_pizza/',views.single_pizza,name='single_pizza'),
    path('single_pizza/<int:pizza_id>/',views.single_pizza,name='single_pizza'),
    path('new_topping/<int:pizza_id>/' ,views.new_topping, name='new_topping'),
    path('new_topping/<int:pizza_id>/' ,views.single_pizza, name='new_topping'),
    path('new_topping/',views.new_topping, name='new_topping'),

]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

