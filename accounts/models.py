from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from budget.models import Budget

# Account model
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)
        Budget.objects.create(
            account = self,
            amount  = 0
        )

    def __str__(self):
        return self.user.username
