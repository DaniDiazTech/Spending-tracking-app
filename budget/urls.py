from django.contrib import admin
from django.urls import path
from . import views

app_name = 'budget'
urlpatterns = [
    # Show budget info, but also create income or expense
    path('', views.HomeView.as_view(), name='home'),
    # list all of the user 
    path('list', views.CompleteListview.as_view(), name='list'),

    # Create new category
    path('category/new', views.CategoryCreateView.as_view(), name='category_new'),

    # Edit Income
    path('income/<int:pk>/', views.IncomeUpdateView.as_view(), name='income_update'),
    # Edit Expense
    path('expense/<int:pk>/', views.ExpenseUpdateView.as_view(), name='expense_update'),

    # Delete income 
    path('income/<int:pk>/delete', views.IncomeDeleteView.as_view(), name='income_delete'),
    # Edit Expense
    path('expense/<int:pk>/delete', views.ExpenseDeleteView.as_view(), name='expense_delete'),

]
