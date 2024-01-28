from django.contrib import admin
from .models import Customer
from .models import Vape
from .models import Product
from .models import Promo
from .models import Order




admin.site.register(Customer)
admin.site.register(Vape)
admin.site.register(Product)
admin.site.register(Promo)
admin.site.register(Order)
