from django.test import TestCase
from income.models import Income


class IncomeTest(TestCase):
    """Test module for Income model"""

    def setUp(self):
        """Set up for test"""
        Income.objects.create(description='Test income', amount=100, sources='Test sources')

    def tearDown(self):
        """Tear down for test"""
        Income.objects.all().delete()

    def test_income_description(self):
        """Test income description"""
        income = Income.objects.get(description='Test income')
        self.assertEqual(income.description, 'Test income')

    def test_income_amount(self):
        """Test income amount"""
        income = Income.objects.get(description='Test income')
        self.assertEqual(income.amount, 100)

    def test_income_sources(self):
        """Test income sources"""
        income = Income.objects.get(sources='Test sources')
        self.assertEqual(income.sources, 'Test sources')

    def test_verbose_name_plural(self):
        """ Test verbose_name_plural method """
        self.assertEqual(str(Income._meta.verbose_name_plural), "Income")
