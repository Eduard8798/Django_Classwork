from django.urls import path
from . import views

urlpatterns = [
    path('',views.Product,name='product_list'),
]