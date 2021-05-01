from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Model to create a pizza
class Pizza(models.Model):
    text = models.CharField(max_length=200)
    # text = models.TextField()
    own = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
# Model for naming the toppings on the pizza
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.TextField()   

    def __str__(self):
        return self.pizza
        return self.name

