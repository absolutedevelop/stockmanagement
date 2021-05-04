from django.db import models

# Create your models here.
class StockItem(models.Model):
	item_description = models.TextField()
	stock_price = models.DecimalField(decimal_places=2,max_digits=10)
	quantity = models.IntegerField()
	slug = models.SlugField()
	scanned_date  = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.item_description




