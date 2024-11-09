from django import forms

from .models import Contracts

class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts  # Модель, для которой создается форма
        fields = ['counthours']  # Поля, которые будут отображаться в форме
