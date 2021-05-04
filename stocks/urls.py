
from django.contrib import admin
from django.urls import path
from . import views 


#routes 
urlpatterns = [
    path('',views.stock_identification),
]
