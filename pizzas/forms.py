from django import forms
from .models import Pizza
from .models import Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        label = {'text ' ':'}