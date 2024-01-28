from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Customer, Order, Product
from .forms import Customerform, OrderForm, LoginForm
from django.contrib import messages 

def customer_page(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {'customers': customers, 'orders': orders}
    return render(request, 'pages/customer.html', context)

def about_page(request):
    return render(request, 'pages/about.html')

def home(request):
    # Assuming you want to display some featured products on the home page
    featured_products = Product.objects.filter(featured=True) 
    context = {
        'featured_products': featured_products,
    }

    return render(request, 'pages/home.html', context)

def create_customer(request):
    if request.method == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_page')  # Redirect to the customer_page after successful form submission
    else:
        form = Customerform()

    context = {'form': form}
    return render(request, 'pages/register.html', context)

def delete_customer(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        customer = Customer.objects.get(pk=customer_id)
        customer.delete()
        return redirect('customer_page')

    customers = Customer.objects.all()
    return render(request, 'pages/delete.html', {'customers': customers})

def success_page(request):
    return render(request, 'pages/sucess.html')

def update_customer(request):
    if request.method == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
            # Assuming you have a unique identifier like email to identify the customer
            email = form.cleaned_data['email']
            customer = Customer.objects.get(email=email)
            form = Customerform(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('customer_page')
    else:
        form = Customerform()

    context = {'form': form}
    return render(request, 'pages/update.html', context)

def order_page(request):
    try:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success_page')  # Replace 'success_page' with the name of your success page URL
            else:
                print(form.errors)  # Add this line to check form errors in your console/terminal
        else:
            form = OrderForm()

        return render(request, 'pages/order.html', {'form': form})
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('customer_page')
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})


def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully.')
            return redirect('customer_page')  # Redirect to the appropriate view
    else:
        form = OrderForm(instance=order)
    
    return render(request, 'pages/update_order.html', {'form': form, 'order': order})

def delete_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return redirect('customer_page')

    return HttpResponse("Invalid request method.")