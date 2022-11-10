from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BudgetView, name='main'),
    path('category/new', views.CategoryCreateView, name='category_new'),
]
