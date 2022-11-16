from django.views.generic import DetailView, CreateView, View, TemplateView, ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Budget, Category, Expense, Income

class BudgetView(LoginRequiredMixin, CreateView):
    login_url = "login/"
    redirect_field_name = 'login'
    template_name = "budget/budget.html"

    model = Expense
    fields = ['name', 'amount', 'category']

    # Get categories
    # Get budget linked to the user
    # Get all expenses and incomes
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['budget'] = get_object_or_404(Budget, user=self.request.user)

        context['expenses'] = get_list_or_404(Expense, budget=context['budget'])
        context['incomes'] = get_list_or_404(Income, budget=context['budget']) 
        return context

        
class CategoryCreateView(CreateView, LoginRequiredMixin):
    model = Category
    template_name = "budget/category-create.html"


class IncomeCreateView(CreateView, LoginRequiredMixin):
    model = Category
    template_name = "bugdet/income-create.html"