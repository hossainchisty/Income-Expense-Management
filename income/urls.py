from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("income/", views.IncomeList.as_view(), name="income"),
    path("income/add/", views.CreateIncome.as_view(), name="addIncome"),
    path("income/delete/<int:pk>/", views.deleteINcome.as_view(), name="delete-income"),
    path("income/update/<int:pk>/", views.UpdateIncome.as_view(), name="update-income"),
    path("export/", views.exportIncome, name="export-income"),
]
