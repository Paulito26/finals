
from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=250, null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=250, blank=True)
    address = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} {self.email}  {self.phone}'
    

class Vape(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    vape = models.ForeignKey(Vape, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='Product/', blank=True)
    featured = models.BooleanField(default=False)  # Add this line for the featured field

    def __str__(self):
        return f'{self.product_name} {self.price}  {self.image}'


class Promo(models.Model):
    Promo_name   = models.CharField(max_length=100, null=True)
    product_name = models.ManyToManyField(Product)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Promo_name

class Order(models.Model):
    product_name = models.ForeignKey(Product,null=True, on_delete= models.SET_NULL)
    Promo_name = models.ForeignKey(Promo,null=True, on_delete= models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    phone = models.IntegerField()
    quantity = models.IntegerField()
    address = models.CharField(max_length=250, null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
          return f'{self.customer} {self.product_name} {self.quantity}'


