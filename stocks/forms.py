from django import forms 
from .models import StockItem
from django.core.mail import send_mail

#get all the stock from the database - for a dropmenu 
items  = StockItem.objects.all()
choice_items  = []
#append the markers on the array - for the Choice field. identification_marker is not a id of the field on the database 
for i in items:
	choice_items.append((i.identification_marker,i.identification_marker))

#form for the drop dowm menu - for selecting the stock
class StockSelectForm(forms.Form):
	#Field for selecting the stock marker
	stock_marker = forms.ChoiceField(choices = choice_items)


#form to enter the quanity of the items
class StockForm(forms.Form):
	#field to enter the quantity
	quantity = forms.IntegerField()

#form to enter the email - for sending the report
class EmailForm(forms.Form):
	#field for entering an email
	email = forms.EmailField();

	#send an email of the stock list - report 
	def send_email(self,email,stock,stock_quantities):
		#create a report to send to the email 
		report = "A Report from the Intern Stock Management App\n\nThe following stock item has been updated!\n";
		items_total = 0; # total of all the stock items 
		report = report + "Stock Code(" + stock.identification_marker + ")\n"
		report = report + "Scanned Date(" + stock.scanned_date.strftime("%Y:%m:%d") + ")\n"
		report = report + "Quantities \n"

		for stock_quant in stock_quantities:
			report = report + "- quantity : " + str(stock_quant.quantity) + ",\t Date added : " + stock_quant.created_at.strftime("%Y:%m:%d") + "\n"
			#calculate the total stock items
			items_total += stock_quant.quantity

		#append the total of stock items to the report string 
		report = report + "\nTotal stock items : " + str(items_total) 
		#email for the app.
		from_email = "stockmanagementsystemintern@gmail.com"
		#title of the email
		email_title = "Stock Management Report"
		#send an email
		send_mail(email_title, report,from_email,[email])






