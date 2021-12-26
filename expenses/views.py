import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Expense


class expenseList(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "expenses/expenses.html"
    context_object_name = "expenselist"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["expenselist"] = Expense.objects.filter(owner=self.request.user)
        return context


class expensesCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Expense
    fields = ["why", "amount", "description"]
    success_url = reverse_lazy("expense")
    template_name = "expenses/addExpenses.html"
    success_message = "Expense successfully created"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(expensesCreate, self).form_valid(form)


class expensesUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ["why", "amount", "description"]
    template_name = "expenses/expenses_form.html"
    success_url = reverse_lazy("expense")
    success_message = "Expense successfully updated"


class expensesDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Expense
    context_object_name = "expenses"
    success_url = reverse_lazy("expense")
    template_name = "expenses/expenses_confirm_delete.html"
    success_message = "Expenses successfully deleted"

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(owner=user)


@login_required(login_url="login")
def exportExpense(request):
    response = HttpResponse(content_type='text/csv')

    w = csv.writer(response)
    w.writerow(['Amount', 'Why', 'Description', 'Time and Date'])

    for expense in Expense.objects.filter(owner=request.user).values_list('amount', 'why',  'description', 'date'):
        w.writerow(expense)

    response['Content-Disposition'] = 'attachment; filename="expenses_summary.csv"'
    return response
