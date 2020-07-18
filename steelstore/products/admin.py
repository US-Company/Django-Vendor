from django.contrib import admin
from .models import Order
from .models import Item
from .models import Account


# Register your models here.

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Account)
