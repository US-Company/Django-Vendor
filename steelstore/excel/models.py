from django.db import models

# Create your models here.

class Export(models.Model):
	time = models.CharField(max_length=50)

	def __str__(self):
		return self.time
