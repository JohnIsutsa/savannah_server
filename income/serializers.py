from income.models import Income
from rest_framework import serializers

class IncomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Income
        fields = ['id', 'source', 'amount', 'description', 'date']