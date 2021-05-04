from django.shortcuts import render
from .models import StockItem
# Create your views here.

def stock_identification(request):

	items  = StockItem.objects.all()

	return render(request,'stocks/stock_identification.html',{'stock_items':items})
