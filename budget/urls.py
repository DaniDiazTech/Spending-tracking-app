from django.contrib import admin
from django.urls import path
from . import views

app_name = 'budget'
urlpatterns = [
    # Show budget info, but also create income or expense
    path('', views.HomeView.as_view(), name='home'),
    # Create new category
    path('category/new', views.CategoryCreateView.as_view(), name='category_new'),

    # Create new Income
    path('income/new', views.IncomeCreateView.as_view(), name='income_new'),

    # Create new Expense
    path('expense/new', views.ExpenseCreateView.as_view(), name='expense_new'),
]
