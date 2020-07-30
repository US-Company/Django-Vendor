from django.db import models
from products.models import Producto

# Create your models here.
class Invoice(models.Model):
	client_name = models.CharField(max_length=50)
	DNI = models.CharField(max_length=10)
	sale_date = models.DateTimeField(editable=False)

class InvoiceItem(models.Model):
	product = models.ForeignKey(Producto)
	factura = models.ForeignKey(Invoice)
	cantidad = models.IntegerField()