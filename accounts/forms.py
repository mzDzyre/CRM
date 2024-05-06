from django.forms import ModelForm, HiddenInput
from django import forms
from .models import Order, Customer


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["customer"].disabled = True

    class Meta:
        model = Order
        fields = "__all__"


class CreateCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
