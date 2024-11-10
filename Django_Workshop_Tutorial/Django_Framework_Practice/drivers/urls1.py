from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("drivers",views.drivers, name='drivers'),
    path('testing', views.testing, name='testing'),
    path("drivers/details/<int:id>", views.details, name='details')
    ]
