from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    # URL для регистрации пользователей
    path('register/', include('djoser.urls')),
    # URL для авторизации по логину и паролю
    path('auth-rest/', include('rest_framework.urls')),
    # URL для создания токена для авторизации пользователя по токену
    path('auth-djoser/', include('djoser.urls.authtoken')),
]
