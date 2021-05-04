
from django.contrib import admin
from django.urls import path, include
from . import views 


#routes 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('stocks.urls')),
    path('about/', views.about ),
    path('',views.homepage),
]
