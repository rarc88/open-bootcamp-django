from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>', views.index, name='index'),
    path('create/', views.create, name='create'),
]
