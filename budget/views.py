from datetime import datetime
from django.urls import reverse_lazy

from django.views.generic import DetailView, CreateView, View, TemplateView, ListView, DeleteView, UpdateView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect


from django.db.models import Sum

from .models import Budget, Category, Expense, Income, User

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

        # only first four
        context['incomes'] = context['incomes'][:4]
        context['expenses'] = context['expenses'][:4]
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
    template_name = "budget/list.html"
    
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
    success_url = reverse_lazy('budget:home')
    fields = ['name']

class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    template_name = "budget/income-update.html"
    fields = ['name', 'description', 'amount', 'category']
    success_url = reverse_lazy('budget:home')

    def get_context_data(self, *args, **kwargs):
        context = super(IncomeUpdateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        t = form.save(commit=False)
        t.budget = Budget.objects.get(user=self.request.user)
        t.save()
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = "budget/expense-update.html"
    fields = ['name', 'description', 'amount', 'category']
    success_url = reverse_lazy('budget:home')

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseUpdateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        t = form.save(commit=False)
        t.budget = Budget.objects.get(user=self.request.user)
        t.save()
        return super().form_valid(form)

class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = "budget/income-delete.html"
    success_url = reverse_lazy('budget:home')

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = "budget/expense-delete.html"
    success_url = reverse_lazy('budget:home')
