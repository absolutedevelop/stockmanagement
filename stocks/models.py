from django.db import models

# model for the stock item
class StockItem(models.Model):
	#identification marker - the stock code
	identification_marker = models.TextField()
	#scanned date 
	scanned_date  = models.DateTimeField(auto_now_add=True)
	#function that print the stock code
	def __str__(self):
		return self.identification_marker

#class for the quanties 
class StockQuantities(models.Model):
	#quantity value
	quantity = models.IntegerField()
	#created at
	created_at = models.DateTimeField(auto_now_add=True)
	#foreign key - represent the stock that quantity belongs to
	stock_item = models.ForeignKey(StockItem, on_delete = models.CASCADE);




