from django.urls import path
from api import views


urlpatterns = [
    path('theAdvert/<int:some_pk>/', views.AdvertAPI.as_view(), name='advertapi'),
]
