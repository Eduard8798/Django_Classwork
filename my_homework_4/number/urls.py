from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.rundom_numbers_many),
    path('', views.rundom_numer_one),
    path('<int:pd>/<int:pk>', views.rundom_numbers_diapazone),

]
