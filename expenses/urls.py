from django.urls import path
from . import views

urlpatterns = [
    path("", views.expenseList.as_view(), name="expense"),
    path("add", views.expensesCreate.as_view(), name="add-expense"),
    path("update/<int:pk>", views.expensesUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.expensesDelete.as_view(), name="delete"),
    path("summary/", views.expenseSummary, name="expense-summary"),
]
