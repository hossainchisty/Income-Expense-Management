from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Income
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required(login_url="login")
def dashboard(request):
    return render(request, "index.html")


class IncomeList(LoginRequiredMixin, ListView):
    model = Income
    template_name = "income/income.html"
    context_object_name = "incomes"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["incomes"] = Income.objects.filter(user=self.request.user)
        return context


class CreateIncome(LoginRequiredMixin, CreateView):
    model = Income
    fields = ["amount", "description", "sources"]
    success_url = reverse_lazy("income")
    template_name = "income/addIncome.html"
    success_message = "Income Created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateIncome, self).form_valid(form)


class UpdateIncome(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ["amount", "description", "sources"]
    success_url = reverse_lazy("income")
    success_message = "Income update successfully"


class deleteINcome(LoginRequiredMixin, DeleteView):
    model = Income
    context_object_name = "incomes"
    success_message = "Income delete successfully"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


@login_required(login_url="login")
def incomeSummary(request):
    return render(request, "income/income_summary.html")


# if request.user.is_authenticated:
#     # Do something for authenticated users.
# else:
#     # Do something for anonymous users.
