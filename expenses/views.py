from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from expenses.models import Expense
from expenses.serializers import ExpensesSerializer
from rest_framework import permissions
from .permissions import IsOwner

# Create your views here.

class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expense.objects.all()
    permission_classes=(permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expense.objects.all()
    permission_classes=(permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)