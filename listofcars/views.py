from django.shortcuts import render
from django.views import View
from .models import Cars, Contracts
class CarView(View):
    def get(self, request):
        post_car = {
            'Cars': Cars.objects.all(),
        }
        return render(request, 'html/index.html', post_car)
