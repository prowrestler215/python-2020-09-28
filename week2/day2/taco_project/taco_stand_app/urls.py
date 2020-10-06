from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('tacos', views.add_a_taco),
]
