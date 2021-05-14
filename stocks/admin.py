from django.contrib import admin
from .models import StockItem,StockQuantities

# Register your models here.
admin.site.register(StockItem)
admin.site.register(StockQuantities)
