from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Avg, Sum, Max, Min, Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.db.models.functions import (
    ExtractDay,
    ExtractHour,
    ExtractMinute,
    ExtractMonth,
    ExtractQuarter,
    ExtractSecond,
    ExtractWeek,
    ExtractIsoWeekDay,
    ExtractWeekDay,
    ExtractIsoYear,
    ExtractYear,
    Extract,
)

from django.db.models import F, Q
import datetime
from django.db import connection
from django.utils import timezone
from django.views.decorators.cache import cache_page
from datetime import timedelta
from datetime import datetime

# Imports models
from .models import Income
from expenses.models import Expense


@login_required(login_url="login")
def dashboard(request):
    expense = Expense.objects.filter(owner=request.user).aggregate(Sum("amount"))
    income = Income.objects.filter(user=request.user).aggregate(Sum("amount"))

    totalbalance = float(expense["amount__sum"]) + float(income["amount__sum"])

    weekly_aggregate = (
        Income.objects.annotate(week=ExtractWeek("date"))
        .values("week")
        .annotate(count=Count("id"))
        .values("week", "count")
    )
    # print(weekly_aggregate)
    # Add the income start year as a field in the QuerySet.
    experiment = Income.objects.annotate(weekday=ExtractWeekDay("date"))

    unique = User.objects.values("is_active").annotate(
        total=Count("id"),
        unique_names=Count("last_name", distinct=True),
    )
    # print(unique)
    # print(experiment)
    # How many experiments completed in the same year in which they started?
    # years = Income.objects.filter(start_datetime__year=Extract("date", "year")).count()
    # print(years)

    testUSer = User.objects.values("date_joined__year").annotate(
        staff_users=(Count("id", filter=Q(is_staff=True))),
        non_staff_users=(Count("id", filter=Q(is_staff=False))),
    )
    # print(testUSer)

    # currentUSer = User.objects.values("date_joined__year").annotate(total=Count("id"))
    # print(currentUSer)
    context = {
        "totolIncome": income["amount__sum"],
        "totalExpense": expense["amount__sum"],
        "total_balance": totalbalance,
    }
    return render(request, "index.html", context)


class IncomeList(LoginRequiredMixin, ListView):
    model = Income
    template_name = "income/income.html"
    context_object_name = "incomes"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["incomes"] = Income.objects.filter(user=self.request.user)
        return context


class CreateIncome(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Income
    fields = ["amount", "description", "sources"]
    success_url = reverse_lazy("income")
    template_name = "income/addIncome.html"
    success_message = "Income successfully created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateIncome, self).form_valid(form)


class UpdateIncome(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Income
    fields = ["amount", "description", "sources"]
    success_url = reverse_lazy("income")
    success_message = "Income successfully updated"


class deleteINcome(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Income
    context_object_name = "incomes"
    success_url = reverse_lazy("income")
    success_message = "Income successfully deleted"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


@login_required(login_url="login")
def incomeSummary(request):
    # if request.user.is_authenticated:
    #     # Do something for authenticated users.
    # else:
    #     # Do something for anonymous users.
    return render(request, "income/income_summary.html")
