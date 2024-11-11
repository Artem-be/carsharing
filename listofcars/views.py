from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cars, Contracts
from .form import ContractsForm
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class CloseContractView(LoginRequiredMixin, View):
    def post(self, request, contract_id):
        contract = get_object_or_404(Contracts, contract_id=contract_id, author=request.user)
        contract.delete()
        return redirect('/')


class CarView(View):
    def get(self, request):
        # Получаем только те автомобили, у которых нет контрактов
        available_cars = Cars.objects.filter(is_reserved=False).exclude(contracts__isnull=False)

        # Условие: показывать контракты только для зарегистрированных пользователей
        available_contracts = []
        if request.user.is_authenticated:
            available_contracts = Contracts.objects.filter(author=request.user)

        context = {
            'Cars': available_cars,
            'Contracts': available_contracts,
        }
        return render(request, 'html/index.html', context)


class ReserveCarView(LoginRequiredMixin, View):  # Используем LoginRequiredMixin здесь
    def get(self, request, car_id):
        car = get_object_or_404(Cars, carid=car_id)
        context = {
            'car': car,
            'form': ContractsForm()
        }
        return render(request, 'html/reserve_car.html', context)

    def post(self, request, car_id):
        car = get_object_or_404(Cars, carid=car_id)
        counthours = ContractsForm(request.POST)

        if counthours.is_valid():
            contract = Contracts.objects.create(
                car=car,
                author=request.user,
                counthours=counthours.cleaned_data['counthours']
            )
            contract.save()
            return redirect('/')  # Перенаправляем на главную страницу

        context = {
            'car': car,
            'form': counthours
        }
        return render(request, 'html/reserve_car.html', context)