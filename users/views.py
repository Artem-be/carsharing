from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View

from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth


'''Класс для авторизации'''


class LoginItemView(View):
    def post(self, request):
        # Обработка формы авторизации
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                # Аутентификация пользователя
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                if user:
                    auth.login(request, user)
                    return HttpResponseRedirect('/')
        else:
            form = UserLoginForm()
            return render(request, 'users/login.html', {'form': form})

    def get(self, request):
        # Вывод формы авторизации
        context = {'form': UserLoginForm()}
        return render(request, 'users/login.html', context)


'''Класс для регистрации'''


class RegisterItemView(View):
    def post(self, request):
        # Обработка формы регистрации
        if request.method == 'POST':
            form = UserRegistrationForm(data=request.POST)
            if form.is_valid():
                # Создание нового пользователя
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = UserRegistrationForm()

    def get(self, request):
        # Вывод формы регистрации
        context = {'form': UserRegistrationForm()}
        return render(request, 'users/register.html', context)