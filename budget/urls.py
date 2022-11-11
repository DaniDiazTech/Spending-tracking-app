from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BudgetView.as_view(), name='budget'),
    path('category/new', views.CategoryCreateView.as_view(), name='category_new'),
    path('income/new', views.IncomeCreateView.as_view(), name='income_new'),
]
