from django.shortcuts import render,redirect
from .forms import *
from OrderManagement.models import *
from CRUD_APP.views import *

# Create your views here.
def AddCustomerPage(request):

    context = {
        'customer_form': Customer_Form()
    }
    
    if request.method == "POST":
        # print(request.POST)
        new_customer = Customer_Form(request.POST)

        if new_customer.is_valid():           
            new_customer.save()
            
    return render(request,'Customers_add.html',context)

def AllCustomer(request):
    context = {
        "All_Customer" : Customer.objects.all()
    }
    return render(request,'Customers.html',context)

def DeleteCustomer(request,id):
    selected_customer = Customer.objects.get(id = id)
    selected_customer.delete()

    return redirect('/order/all/customer/')

#Update btn
def UpdateCustomer(request,id):
    update_product = Customer.objects.get(id = id)

    context = {
        "product_form" : Customer_Form(instance=update_product)
    }
    if request.method == "POST":
        update_btn =  Customer_Form(request.POST,instance=update_product)
        if update_btn.is_valid():
            update_btn.save()

            return redirect('/order/all/customer/')

        
    return render(request,"Customer_add.html",context)

def OrdersAdd(request):
    context = {
        'order_form': Orders_Form()
    }
    if request.method == "POST":

        # print(request.POST)
        selected_product = Product.objects.get(id = request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        # qty=int(selected_product.qty) - int(request.POST['quantity'])
        # # qty.save()
        # UpdateProducts(request,selected_product.id)

        gst_amount = (amount * selected_product.gst)/100
        bill_amount = amount + gst_amount

        new_order = Orders(customer_reference_id = request.POST['customer_reference'],product_reference_id = request.POST['product_reference'],order_number = request.POST['order_number'],order_date = request.POST,quantity = request.POST['quantity'],amount = amount, gst_amount = gst_amount, bill_amount = bill_amount)

        new_order.save()

    return render(request, 'Orders.html',context)