from django.db import models
from django.utils import timezone
# Create your models here.


class Item(models.Model):

	category = models.CharField(max_length=225)
	isbn = models.CharField(max_length=225)
	create = models.DateTimeField(editable=False)
	price = models.DecimalField(decimal_places=2, max_digits=6)
	stock_level = models.IntegerField()

	def __str__(self):
		return self.category

	def save(self, *args, **kwargs):
		if not self.id:
			self.create = timezone.now()
		return super(Item, self).save(*args, **kwargs)


class Account(models.Model):

	creation_date = models.DateTimeField(editable=False)
	e_mail = models.EmailField()
	user_name = models.CharField(max_length=11)
	password = models.CharField(max_length=50)
	active = models.BooleanField()

	def __str__(self):
		return str(self.user_name)

	def save(self, *args, **kwargs):
		if not self.id:
			self.creation_date = timezone.now()
		return super(Account, self).save(*args, **kwargs)