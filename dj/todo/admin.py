from django.contrib import admin
from .models import Todo

# Register your models here.

# admin.site.register(Todo)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Todo._meta.get_fields()]