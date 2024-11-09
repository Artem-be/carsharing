from django.urls import path
from .views import CarView, LogoutView,ReserveCarView

urlpatterns = [
    path('', CarView.as_view(), name='home'),
    path('reserve_car/<int:car_id>/', ReserveCarView.as_view(), name='reserve_car'),
    path('logout/', LogoutView.as_view(), name='logout')
]