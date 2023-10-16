from . import views
from django.contrib import admin
from django.urls import path, include
urlpatterns =[
    path('', views.data_and_charts, name='task_list'),
]