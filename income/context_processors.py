from .models import Income
from django.db.models import Avg, Sum, Max, Min, Count


# def getIncomeData(request):

#     income = Income.objects.filter(user=request.user).aggregate(Sum("amount"))

#     context = {
#         "totolIncome": income["amount__sum"],
#     }

#     return context
