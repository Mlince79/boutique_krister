from django.urls import path
from .import views

urlpatterns = [
    path('', views.chekout, name='checkout'),
]