from django.shortcuts import render, redirect
from .models import *
from .forms import *


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
    # customers = Customer.objects.all()
    # orders = Order.objects.all()
    # total_orders = orders.count()
    # pending_orders = Order.objects.filter(status="Pending").count()
    # delivered_orders = Order.objects.filter(status="Delivered").count()
    if request.method == 'POST':
        data = request.POST
        form = CreateCustomer(data)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        # "customers": customers,
        # "orders": orders,
        # "total_orders": total_orders,
        # "pending_orders": pending_orders,
        # "delivered_orders": delivered_orders,
        "form": form
    }
    return render(request, "accounts/createCustomer.html", context)


def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        data = request.POST
        form = OrderForm(data)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
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
