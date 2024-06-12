from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('get_exchange_rates/', views.get_exchange_rates)
]

