from django.shortcuts import render, redirect
from django.views import View
from .models import Cars, Contracts
from django.contrib.auth import logout
from .form import ContractsForm
class CarView(View):
    def get(self, request):
        post_car = {
            'Cars': Cars.objects.all(),
        }
        return render(request, 'html/index.html', post_car)

class LogoutView(View):
    '''Выход пользователя из системы'''
    def get(self, request):
        logout(request)
        return redirect('home')


class ReserveCarView(View):
    def get(self, request, car_id):
        car = Cars.objects.get(carid=car_id)
        context = {
            'car': car,
            'form': ContractsForm()  # Передаем пустую форму
        }
        return render(request, 'html/reserve_car.html', context)

    def post(self, request, car_id):
        user = request.user
        car = Cars.objects.get(carid=car_id)
        counthours = ContractsForm(request.POST)  # Создаем форму с данными из POST запроса
        if counthours.is_valid():
            counthours.save(commit=False)  # Создаем объект, но не сохраняем его
            counthours.car = car  # Устанавливаем машину
            counthours.author = user  # Устанавливаем пользователя
            counthours.save()  # Сохраняем объект
            return redirect('/')

        context = {
            'car': car,
            'form': counthours
        }
        return render(request, 'html/reserve_car.html', context)