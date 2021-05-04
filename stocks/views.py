from django.shortcuts import render

# Create your views here.

def stock_identification(request):
	return render(request,'stocks/stock_identification.html')
