
from django.contrib import admin
from django.urls import path
from . import views 


#routes 
urlpatterns = [
    path('',views.stock_identification),
    path('report/send/<str:stock_marker>',views.send_email_report),
    path('<str:stock_marker>',views.single_stock),

]
