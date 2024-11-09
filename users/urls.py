from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Определение URL-шаблонов для приложения
urlpatterns = [
    # URL для авторизации
    path('login/', views.LoginItemView.as_view(), name='login'),

    # URL для регистрации
    path('register/', views.RegisterItemView.as_view(), name='register'),
]

# Добавление URL для статических файлов в режиме отладки
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)