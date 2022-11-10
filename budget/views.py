from django.views.generic import DetailView, CreateView, View
from .models import Budget, Category, Expense, Income

class BudgetView(View):
    pass     

class CategoryCreateView(CreateView):
    model = Category
    template_name = ".html"
