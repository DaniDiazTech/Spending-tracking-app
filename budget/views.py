from datetime import datetime

from django.views.generic import DetailView, CreateView, View, TemplateView, ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect


from django.db.models import Sum

from .models import Budget, Category, Expense, Income

from .forms import IncomeForm, ExpenseForm

class HomeView(LoginRequiredMixin, View):
    template_name = "budget/home.html"
    fields = ['name', 'amount', 'category']

    # Get categories
    # Get budget linked to the user
    # Get all expenses and incomes
    def get(self, *args, **kwargs): 
        context = {}
        context['categories'] = Category.objects.all()
        context['budget'] = Budget.objects.get(user=self.request.user)
        current_month = datetime.now().month
        # Only gets expenses and incomes from current month
        context['expenses'] = Expense.objects.filter(budget=context['budget'], updated__month = current_month)
        context['incomes'] = Income.objects.filter(budget=context['budget'], updated__month = current_month)
        context['sum_expenses'] = context['expenses'].aggregate(Sum('amount'))['amount__sum']
        if (context['sum_expenses'] is None):
            context['sum_expenses'] = 0
        context['sum_incomes'] = context['incomes'].aggregate(Sum('amount'))['amount__sum']

        if (context['sum_incomes'] is None):
            context['sum_incomes'] = 0

        context['budget_amount'] = context['sum_incomes'] -  context['sum_expenses']

        # Forms
        context['expense_form'] = ExpenseForm
        context['income_form'] = IncomeForm

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        if "income" in self.request.POST:
            form = IncomeForm(self.request.POST)
            if form.is_valid():
                temp = form.save(commit=False)
                temp.budget = Budget.objects.get(user=self.request.user)
                temp.save()
                
        elif "expense" in self.request.POST:
            form = ExpenseForm(self.request.POST)
            if form.is_valid():
                temp = form.save(commit=False)
                temp.budget = Budget.objects.get(user=self.request.user)
                temp.save()
        
        return redirect('budget:home')
            
class CompleteListview(LoginRequiredMixin, View):
    
    # Get all expenses and incomes of the user
    def get(self, *args, **kwargs): 
        context = {}
        context['categories'] = Category.objects.all()
        context['budget'] = get_object_or_404(Budget, user=self.request.user)

        context['expenses'] = Expense.objects.filter(budget=context['budget'])
        context['incomes'] = Income.objects.filter(budget=context['budget']) 
        return render(self.request, self.template_name, context)
        
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "budget/category-create.html"


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    template_name = "bugdet/income-create.html"

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = "bugdet/expense-create.html"

