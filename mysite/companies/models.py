import datetime

from django.db import models
from django.utils import timezone


class Companies(models.Model):
    company_name = models.CharField(max_length=200)
    company_owner = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date creation")
    def __str__(self):
        return self.company_name


class Employees(models.Model):
    company = models.ForeignKey('companies.Companies', on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=200)
    employee_job = models.CharField(max_length=200)
    def __str__(self):
        return self.employee_name