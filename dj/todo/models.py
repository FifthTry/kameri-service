from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=1024)
    status = models.CharField(max_length=1024)
    tracker = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
