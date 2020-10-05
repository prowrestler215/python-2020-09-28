from django.urls import include, path

from . import views

urlpatterns = [
    # will render a template
    path('', views.index),
    path('success', views.success),


    # will redirect to a template
    path('login', views.login),
    path('logout', views.logout),
]
