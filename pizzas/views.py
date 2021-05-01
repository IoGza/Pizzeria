from django.shortcuts import render,redirect
from .models import Pizza
from .models import Topping
from .forms import PizzaForm
from .forms import ToppingForm
from django.contrib.auth.decorators import login_required
from django.http import Http404



# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')
@login_required
def pies(request):
    pizzas = Pizza.objects.filter(own=request.user)

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html',context)


@login_required
def single_pizza(request,pizza_id):
    pie = Pizza.objects.get(id=pizza_id)
    top = pie.topping_set

    if pie.own != request.user:
        raise Http404

    context = {'pie':pie,'top':top}

    return render(request, 'pizzas/single_pizza.html',context)

@login_required
def new_pizza(request):
    # pie = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.own = request.user
            new_pizza.save()
            form.save()
            return redirect('pizzas:pizzas')
            
    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html',context)


@login_required
def new_topping(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if pizza.own != request.user:
        raise Http404

    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()

            return redirect('pizzas:pizzas', pizza_id = pizza_id)
    context = {'pizza':pizza,'form':form }
    return render(request,'pizzas/new_topping.html',context)

