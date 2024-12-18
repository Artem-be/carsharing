from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import ContractsForm, CarForm
from django.contrib.auth import logout
from .dal import (
    get_available_cars, get_user_contracts, create_contract, get_car_by_id,
    delete_contract, create_car, delete_car, get_car_for_edit, update_car
)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class CloseContractView(LoginRequiredMixin, View):
    def post(self, request, contract_id):
        delete_contract(contract_id, request.user)
        return redirect('/')

class CarView(View):
    def get(self, request):
        available_cars = get_available_cars()
        available_contracts = get_user_contracts(request.user)
        context = {'Cars': available_cars, 'Contracts': available_contracts}
        return render(request, 'html/index.html', context)

class ReserveCarView(LoginRequiredMixin, View):
    def get(self, request, car_id):
        car = get_car_by_id(car_id)
        context = {'car': car, 'form': ContractsForm()}
        return render(request, 'html/reserve_car.html', context)

    def post(self, request, car_id):
        car = get_car_by_id(car_id)
        form = ContractsForm(request.POST)
        if form.is_valid():
            create_contract(car, request.user, form.cleaned_data['counthours'])
            return redirect('/')
        context = {'car': car, 'form': form}
        return render(request, 'html/reserve_car.html', context)

class AddCar(View):
    def get(self, request):
        form = CarForm()
        return render(request, 'html/add_car.html', {'form': form})

    def post(self, request):
        form = CarForm(request.POST)
        if form.is_valid():
            create_car(form.cleaned_data, request.user)
            return redirect('home')
        return render(request, 'html/add_car.html', {'form': form})

class DeleteCar(View):
    def post(self, request, car_id):
        delete_car(car_id)
        return redirect('home')

class EditCar(View):
    def get(self, request, car_id):
        car = get_car_for_edit(car_id)
        form = CarForm(instance=car)
        return render(request, 'html/edit_car.html', {'form': form})

    def post(self, request, car_id):
        form = CarForm(request.POST, instance=get_car_for_edit(car_id))
        if form.is_valid():
            update_car(car_id, form.cleaned_data)
            return redirect('home')
        return render(request, 'html/edit_car.html', {'form': form})