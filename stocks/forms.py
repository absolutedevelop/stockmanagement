from django import forms 
from .models import StockItem


items  = StockItem.objects.all()

choice_items  = []

for i in items:
	choice_items.append((i.identification_marker,i.identification_marker))

class StockSelectForm(forms.Form):
	stock_marker = forms.ChoiceField(choices = choice_items)


class StockForm(forms.Form):

	quantity = forms.IntegerField()