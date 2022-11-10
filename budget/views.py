from django.views.generic import DetailView, CreateView, View
from .models import Budget, Category, Expense, Income

class BudgetView(View):
    # Get categories
    # Get account info
    # Get budget linked to the account
    # Get all expenses and incomes
    def get(self, request, *args, **kwargs):
        pass

        
class CategoryCreateView(CreateView):
    model = Category
    template_name = ".html"

class ExpenseCreateView(CreateView):
    model = Category
    template_name = ".html"

class IncomeCreateView(CreateView):
    model = Category
    template_name = ".html"