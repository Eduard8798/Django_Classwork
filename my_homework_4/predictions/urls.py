from django.urls import path
from .views import PostRandom,PredictView


urlpatterns = [
    path('', PredictView.as_view(), name='predict'),
    path('<int:pk>/', PostRandom.as_view(), name='post_random'),
]
