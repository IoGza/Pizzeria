from django.db import models

# Create your models here.

# Model to create a pizza
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    # owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# Model for naming the toppings on the pizza
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.TextField()   

    def __str__self(self):
        return self.pizza
        return self.name