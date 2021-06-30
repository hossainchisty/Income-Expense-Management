from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Expense


class expenseList(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "expenses/expenses.html"
    context_object_name = "expenselist"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["expenselist"] = Expense.objects.filter(owner=self.request.user)
        return context


class expensesCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ["name", "amount", "description"]
    success_url = reverse_lazy("expense")
    template_name = "expenses/addExpenses.html"
    success_message = "Expense Created successfully"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(expensesCreate, self).form_valid(form)


class expensesUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ["name", "amount", "description"]
    template_name = "expenses/expenses_form.html"
    success_url = reverse_lazy("expense")
    success_message = "Expense Created successfully"


class expensesDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    context_object_name = "expenses"
    # template_name = "expenses/expenses_confirm_delete.html"
    success_message = "Expenses delete successfully"

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(owner=user)


@login_required(login_url="login")
def expenseSummary(request):
    return render(request, "expenses/expenses_summary.html")
