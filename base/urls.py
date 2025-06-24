from django.urls import path
from . import views


# path is used as url route
# here, the base path calls views.home function
urlpatterns = [
    path('', views.home, name="home"),
]
