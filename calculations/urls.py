from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_view, name='calculate'),
    path('diagnostic/', views.diagnostic_view, name='diagnostic'),
]
