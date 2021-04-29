from django.shortcuts import render,redirect
from .models import Pizza
from .models import Topping
from .forms import PizzaForm

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html',context)

def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()        
            form.save()

            return redirect('pizzas:new_pizza')
    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html',context)
