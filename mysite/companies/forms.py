from django import forms
from .models import Companies, Employees

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['company_name', 'company_owner', 'creation_date']

class EmployeeForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Companies.objects.all())
    class Meta:
        model = Employees
        fields = ['company','employee_name', 'employee_job']
