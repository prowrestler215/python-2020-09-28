from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('thursday', views.show_thursday),
    path('redirect', views.demo_redirect),

    path('day/<str:some_day>', views.display_day),
    # path('day/tuesday', views.demo_redirect),
    # path('day/wendesday', views.demo_redirect),
]
