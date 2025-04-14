from django.urls import path
from .views import PredictTraffic

urlpatterns = [
    path('predict/', PredictTraffic.as_view(), name='predict'),
]
