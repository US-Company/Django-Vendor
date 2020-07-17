from django.db import models

# Create your models here.

class Item(models.Model):

	category = models.CharField(max_length=225)
	isbn = models.CharField(max_length=225)
	create = models.DateTimeField()
	price = models.DecimalField(decimal_places=2, max_digits=6)
	stock_level = models.IntegerField()

	def __str__(self):
		return self.category
#
class Account(models.Model):

	creation_date = models.DateTimeField()
	e_mail = models.EmailField()
	user_name = models.CharField(max_length=11)
	password = models.CharField(max_length=50)
	active = models.BooleanField()

	def __str__(self):
		return self.creation_date