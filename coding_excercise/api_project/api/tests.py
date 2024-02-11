# api/tests.py

from django.test import TestCase
from .models import Company, Client, ClientUser
from django.contrib.auth.models import User

class CompanyTestCase(TestCase):
    def test_more_than_200000_employees(self):
        companies = Company.objects.filter(employees__gt=200000)
        self.assertEqual(companies.count(), 1)

    # Define other test cases as required
