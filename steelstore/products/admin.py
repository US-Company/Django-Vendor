from django.contrib import admin
from .models import Order
from .models import Producto
from .models import Account


# Register your models here.

admin.site.register(Order)
admin.site.register(Producto)
admin.site.register(Account)
