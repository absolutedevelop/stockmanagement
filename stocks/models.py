from django.db import models

# Create your models here.
class StockItem(models.Model):
	quantity = models.IntegerField()
	identification_marker = models.TextField()
	scanned_date  = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.identification_marker




