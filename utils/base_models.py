from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    
    class Meta:
        abstract = True
        ordering = ['-created']