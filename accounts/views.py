from django.shortcuts import render, redirect
from .models import *
from .forms import *


def userLogin(request):
    context = {}
    return render(request, 'accounts/login.html',context)

def userRegister(request):
    context = {}
    return render(request, 'accounts/register.html',context)

def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    pending_orders = Order.objects.filter(status="Pending").count()
    delivered_orders = Order.objects.filter(status="Delivered").count()

    context = {
        "customers": customers,
        "orders": orders,
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "delivered_orders": delivered_orders,
    }
    return render(request, "accounts/dashboard.html", context)


def product(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", context={"products": products})


def customer(request, id):
    customers = Customer.objects.get(id=id)
    orders = customers.order_set.all()
    total_orders = orders.count()
    context = {"customers": customers, "orders": orders, "total_orders": total_orders}
    return render(request, "accounts/customer.html", context)


def createCustomer(request):
    form = CreateCustomer()
    if request.method == "POST":
        data = request.POST
        form = CreateCustomer(data)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/createCustomer.html", context)


def createOrder(request, pk):
    """AI is creating summary for createOrder

    Args:
        request ([type]): [description]
        pk ([type]): [description]

    Returns:
        [type]: [description]
    """
    customer = Customer.objects.get(id=pk)
    userform = OrderForm(initial={"customer": customer})
    if request.method == "POST":
        data = request.POST
        form = OrderForm(data, initial={"customer": customer})
        if form.is_valid():
            form.save()
            orders = customer.order_set.all()
            total_orders = orders.count()
            context = {
                "customers": customer,
                "orders": orders,
                "total_orders": total_orders,
            }
            return render(request, "accounts/customer.html", context)

        else:
            print(data)
            print("not valid")
    context = {"form": userform}
    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        data = request.POST
        form = OrderForm(data, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {
        "order": order,
    }
    if request.method == "POST":
        data = request.POST
        order.delete()
        return redirect("/")
    return render(request, "accounts/delete.html", context)
