from unicodedata import category
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True,
                                   null=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name



class Budget(models.Model):
    account  = models.OneToOneField('accounts.Account', on_delete=models.CASCADE)
    amount  = models.DecimalField(max_digits=16, decimal_places=2, default=0)

    def __str__(self):
        return str(self.account) + " - Budget"


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Income(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="income")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    
