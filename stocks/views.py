from django.shortcuts import render,redirect
from .forms import StockSelectForm,StockForm, EmailForm
from .models import StockItem, StockQuantities
from django.http import HttpResponse
import datetime

#view to select the stock items
def stock_identification(request):
	#check if data is posted 
	if request.method == "POST":
		#create a form based on the posted data
		form = StockSelectForm(request.POST)
		#check if the form is valid
		if form.is_valid():
			#get the identification marker for the stock item form the form
			stock_marker = form.cleaned_data["stock_marker"]
			#redirect to another page with the identifer - (not the unique ID in the database)
			response  = redirect("/stock/" + stock_marker)
			#return the reponse
			return response
	#create a form to select the stock
	form = StockSelectForm()
	#render the template and pass the form
	return render(request,'stocks/stock_identification.html',{'form':form})


def single_stock(request,stock_marker):

	#get the stock 
	stock = StockItem.objects.get(identification_marker = stock_marker)
	#check if data has been posted 
	if request.method == "POST":
		#create a form based on posted data
		form = StockForm(request.POST)
		#check if the form is valid 
		if form.is_valid():
			#get a the quantity from the form
			quant = form.cleaned_data["quantity"]
			#set the scanned date
			stock.scanned_date = datetime.datetime.now()
			#save the stock with the new scanned date
			stock.save()

			#create a stock quantity
			stock_quantity = StockQuantities.objects.create(quantity= quant, stock_item=stock)
			#save the stock quantity
			stock_quantity.save()

			#redirect to the send email page
			response  = redirect("report/send/" + stock_marker)
			return response

	#create a form for the stock quantiry
	form = StockForm()
	#render the page and pass the form to the template 
	return render(request,'stocks/stock_quantity.html',{'form':form})


def send_email_report(request, stock_marker):

	#get the stock list 
	stock = StockItem.objects.get(identification_marker = stock_marker)

	#get the stock quantities 
	stock_quantities  = stock.stockquantities_set.all();

	#check if the form has been submitted.
	if request.method == "POST":
		#create a form and past the POST data.
		form  = EmailForm(request.POST)
		#check if the form is valid 
		if form.is_valid():
			#get the email 
			email = form.cleaned_data["email"]
			#send the email 
			form.send_email(email, stock, stock_quantities)	
			#redirect to the home page 
			response  = redirect("/")
			return response
	#create a an email form
	email_form = EmailForm();
	#render the template- and pass the email form 
	return render(request,'stocks/report.html', {"form" : email_form})
