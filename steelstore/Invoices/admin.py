from django.contrib import admin
from .models import InvoiceItem
from .models import Invoice
# Register your models here.

admin.site.register(InvoiceItem)
admin.site.register(Invoice)
