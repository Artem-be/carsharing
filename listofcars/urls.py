from django.urls import path
from .views import CarView

urlpatterns = [
    path('', CarView.as_view(), name='home')
]