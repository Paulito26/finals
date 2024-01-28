from django.urls import path
from .views import customer_page, create_customer, delete_customer, update_customer, order_page, login_view   
from . import views

urlpatterns = [
     path('', views.home, name="home"),
     path('customer/', customer_page, name="customer_page"),
     path('register/', create_customer, name="create_customer"),
     path('customer/update/', views.update_customer, name='update_customer'),
     path('customer/delete/', views.delete_customer, name='delete_customer'),
     path('about/', views.about_page, name="Aboutpage" ),
     path('order/', order_page, name='order_page'),
     path('success/', views.success_page, name='success_page'),
     path('login/', login_view, name='login'),
     path('delete_order/', views.delete_order, name='delete_order'),
     path('update_order/<int:order_id>/', views.update_order, name='update_order'),
     path('delete_order/', views.delete_order, name='delete_order'),
]