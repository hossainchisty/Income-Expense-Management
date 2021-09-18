from django.test import TestCase
from expenses.models import Expense


class ExpenseTest(TestCase):
    """Test module for Expense model"""

    def setUp(self):
        """Set up for tests"""
        Expense.objects.create(
            why='Test expense',
            amount=100,
            description='Test description'
        )

    def tearDown(self):
        """Tear down for tests"""
        Expense.objects.all().delete()

    def test_expense_why(self):
        """Test why property"""
        expense = Expense.objects.get(why='Test expense')
        self.assertEqual(expense.why, 'Test expense')

    def test_expense_amount(self):
        """Test amount property"""
        expense = Expense.objects.get(why='Test expense')
        self.assertEqual(expense.amount, 100)

    def test_expense_description(self):
        """Test description property"""
        expense = Expense.objects.get(why='Test expense')
        self.assertEqual(expense.description, 'Test description')

    def test_expense_string_representation(self):
        """Test the expense string representation"""
        expense = Expense.objects.get(why='Test expense')
        self.assertEqual(str(expense), expense.why)

    def test_verbose_name_plural(self):
        """ Test verbose_name_plural """
        self.assertEqual(str(Expense._meta.verbose_name_plural), "Expense")
