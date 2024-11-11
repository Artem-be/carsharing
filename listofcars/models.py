from django.db import models
from django.conf import settings
class Cars(models.Model):
    carid = models.IntegerField('ID',unique=True)
    make = models.CharField('Марка', max_length=255)
    model = models.CharField('Модель', max_length=255)
    year = models.IntegerField('Год выпуска')
    description = models.TextField('описание автомобиля')
    is_reserved = models.BooleanField(default=False)
    cost_per_hour = models.IntegerField('Стоимость за час')
    created_at = models.DateTimeField('дата и время создания записи', auto_now_add=True)
    updated_at = models.DateTimeField('дата и время последнего обновления записи', auto_now=True)

    def __str__(self):
        return f'{self.make},{self.model}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Contracts(models.Model):

    counthours = models.IntegerField('Кол часов')
    car = models.ForeignKey('Cars', verbose_name='Машина', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True)
    contract_id = models.AutoField(primary_key=True)
    def __str__(self):
        return f'Контракт для {self.car} от {self.author}'

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'



