from django.db import models
from django.utils.text import slugify
from utils.base_models import BaseModel
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
User = get_user_model()

class Category(BaseModel):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name



class Budget(BaseModel):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    amount  = models.DecimalField(max_digits=16, decimal_places=2, default=0)

    def __str__(self):
        return str(self.user) + " - Budget"


@receiver(post_save, sender=User)
def create_budget(sender, instance=None, created=False, **kwargs):
    """
    Create budget whenever a user is created.
    """
    if created:
        Budget.objects.create(user = instance)


class Expense(BaseModel):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Income(BaseModel):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="income")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
   

    def __str__(self):
        return self.name
    
