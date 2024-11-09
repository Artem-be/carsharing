from django.shortcuts import render, redirect
from django.views import View
from .models import Cars, Contracts
from django.contrib.auth import logout
from .form import ContractsForm


class CarView(View):
    def get(self, request):
        # Получаем только те автомобили, у которых нет контрактов
        available_cars = Cars.objects.filter(is_reserved=False).exclude(contracts__isnull=False)

        context = {
            'Cars': available_cars,
        }
        return render(request, 'html/index.html', context)
class ReserveCarView(View):
    def get(self, request, car_id):
        car = Cars.objects.get(carid=car_id)
        context = {
            'car': car,
            'form': ContractsForm()
        }
        return render(request, 'html/reserve_car.html', context)

    def post(self, request, car_id):
        user = request.user
        car = Cars.objects.get(carid=car_id)
        counthours = ContractsForm(request.POST)
        if counthours.is_valid():
            contract = Contracts.objects.create(
                car=car,
                author=user,
                counthours=counthours.cleaned_data['counthours']
            )
            contract.save()
            return redirect('/')  # Перенаправляем на главную страницу
        context = {
            'car': car,
            'form': counthours
        }
        return render(request, 'html/reserve_car.html', context)
class LogoutView(View):
    '''Выход пользователя из системы'''
    def get(self, request):
        logout(request)
        return redirect('home')


