from django import forms
from .models import Pizza
from .models import Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        label = {'Text' ':'}

class ToppingForm(forms.ModelForm):
    class Meta:
        fields = ['text']   
        label = {'Text' ':'}

        widgets = {'text' : forms.Textarea(attrs={'cols':80})}