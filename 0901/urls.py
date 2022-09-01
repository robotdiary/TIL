from django.urls import path
from . import views

app_name = 'melons'
urlpatterns = [
    path('articles/', views.articles, name="articles"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/update/', views.update, name="update")
]