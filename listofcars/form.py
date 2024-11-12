from django import forms

from .models import Contracts, Cars


class CarForm(forms.ModelForm):
    """
    Форма для создания и редактирования записей в модели Car.
    """
    class Meta:
        """
        Метакласс, определяющий настройки формы.
        """
        model = Cars  # Модель, для которой создается форма
        fields = ['make', 'model', 'year', 'description','cost_per_hour']  # Поля, которые будут отображаться в форме

class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts  # Модель, для которой создается форма
        fields = ['counthours']  # Поля, которые будут отображаться в форме
