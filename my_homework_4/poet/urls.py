from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_poets, name='random_poem'),
    path('randompoet/', views.random_poem, name='random_poem'),
    path('<int:pk>/', views.delete_poem, name='delete_poem'),
    #path('/<str:author_name>/', views.random_poem_by_author, name='random_poem_by_author'),
]
