from django.db import models

# Create your models here.

class Item(models.Model):

	category = models.CharField(max_length=225)
	isbn = models.CharField(max_length=225)
	create = models.DateTimeFiecategory
	price = models.DecimalField(decimal_places=2, max_digits=6)
	stock_level = models.IntegerField()

	def __str__(self):
		return self.category