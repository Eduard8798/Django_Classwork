from django.urls import path
from .views import create_car, get_single_car,update_car,delete_car,get_all_cars

urlpatterns = [
    path('create/', create_car),
    path('<int:pk>/', get_single_car),

    path('update/<int:pk>/',update_car),

    path('delete/<int:pk>/',delete_car),
    path('getall/',get_all_cars),
]