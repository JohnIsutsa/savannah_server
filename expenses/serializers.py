from expenses.models import Expense
from rest_framework import serializers

class ExpensesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ['id', 'category', 'amount', 'description', 'date']