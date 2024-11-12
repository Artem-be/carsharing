from django.urls import path
from .views import CarView, LogoutView,ReserveCarView, CloseContractView, AddCar, DeleteCar, EditCar

urlpatterns = [
    path('', CarView.as_view(), name='home'),
    path('reserve_car/<int:car_id>/', ReserveCarView.as_view(), name='reserve_car'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('close_contract/<int:contract_id>/', CloseContractView.as_view(), name='close_contract'),
    path('add/', AddCar.as_view(), name='add_car'),
    path('delete/<int:car_id>/', DeleteCar.as_view(), name='delete_car'),
    path('edit_car/<int:car_id>/', EditCar.as_view(), name='edit_car'),
]