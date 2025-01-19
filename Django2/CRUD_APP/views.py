from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

def HomePage(request):
    data = {
         'name': 'praveen',
         'role': 'admin',
         'marks': [67,95,49,70,37],
    }
   

    return render(request,'Home.html',data)

def AboutPage(request):
    return render(request,'About.html')

def ContactPage(request):
    return render(request,'Contact.html')

def ServicesPage(request):
    return render(request,'Services.html')

def AddProductsPage(request):

    context = {
        'product_form': Product_Form()
    }
    if request.method == "POST":
        add_btn = Product_Form(request.POST)

        if add_btn.is_valid():
            add_btn.save()
            
    return render(request,'AddProducts.html',context)

def AllProducts(request):
    context = {
        "All_Products" : Product.objects.all()
    }
    return render(request,'Products.html',context)

def DeleteProducts(request,id):
    selected_product = Product.objects.get(id = id)
    selected_product.delete()

    return redirect('/crud_app/products/')

