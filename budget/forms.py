from django import forms
from .models import Expense, Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['name',  'description', 'amount', 'category']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'description', 'amount', 'category']