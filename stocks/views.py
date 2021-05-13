from django.shortcuts import render,redirect
from .forms import StockSelectForm,StockForm
from .models import StockItem
from django.http import HttpResponse

import datetime
# Create your views here.

def stock_identification(request):

	if request.method == "POST":
		form = StockSelectForm(request.POST)
		if form.is_valid():

			stock_marker = form.cleaned_data["stock_marker"]
			response  = redirect("/stock/" + stock_marker)
			return response


	form = StockSelectForm()

	return render(request,'stocks/stock_identification.html',{'form':form})


def single_stock(request,stock_marker):

	#get the stock 
	stock = StockItem.objects.get(identification_marker = stock_marker)
	
	
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			print(stock.scanned_date)
			quantity = form.cleaned_data["quantity"]
			stock.quantity = quantity
			#stock.scanned_date = datetime.datetime.now().date()
			stock.save()
			


	form = StockForm()

	return render(request,'stocks/stock_quantity.html',{'form':form})


def send_email_report(request):

	from_email = "stockmanagementsystemintern@gmail.com"
	#send an email
	send_mail(

		"Stock Management Report",

		"Hey form app",

		from_email,

		["mathalefortunate5@gmail.com"]

	)

	return render(request,'stocks/report.html')
