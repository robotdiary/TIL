from django.urls import path
from . import views

app_name = 'apples'
urlpatterns = [
    path('', views.main, name="main"),
]