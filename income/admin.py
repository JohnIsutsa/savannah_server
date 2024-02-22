from django.contrib import admin

from income.models import Income

# Register your models here.

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['amount', 'source', 'description', 'owner']
    search_fields = ['amount', 'source', 'description', 'owner']
    list_filter = ['amount', 'source', 'description', 'owner']