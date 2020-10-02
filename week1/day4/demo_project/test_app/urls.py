from django.urls import path

from . import views

urlpatterns = [
    # these paths render templates
    path('', views.index),
    path('thursday', views.show_thursday),
    path('day/<str:some_day>', views.display_day),

    # these paths return redirects
    path('redirect', views.demo_redirect),
    # path('day/tuesday', views.demo_redirect),
    # path('day/wendesday', views.demo_redirect),
]
