from django import forms
from django.forms import ModelForm
from .models import Order, Product, Customer
from django.contrib.auth.forms import AuthenticationForm

class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product_name', 'Promo_name', 'phone', 'quantity', 'address']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.Select(attrs={'class': 'form-control'}),
            'Promo_name': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )