from .models import Expense
from django.db.models import Avg, Sum, Max, Min, Count


# def getExpenseData(request):

#     expense = Expense.objects.filter(owner=request.user).aggregate(Sum("amount"))

#     context = {"totalExpense": expense["amount__sum"]}

#     return context
