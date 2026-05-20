from django.shortcuts import render, redirect, get_object_or_404
from urllib3 import request
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/prod_list.html', {'products': products})

@login_required(login_url='login') 
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'inventory/prod_form.html', {'form': form})


@login_required(login_url='login')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/prod_form.html', {'form': form})


@login_required(login_url='login')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'inventory/product_delete.html', {'product': product})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):

    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):


        if 'next' in request.GET:
            messages.warning(
                request,
                "Please login to access inventory pages."
            )

        return super().dispatch(request, *args, **kwargs)