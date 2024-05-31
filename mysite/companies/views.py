from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Companies, Employees
from .forms import CompanyForm, EmployeeForm

#################################################### company views

def index(request):
    return HttpResponse("Hello. Welcome to my technical test.")

def company_list(request):
    companies = Companies.objects.all()
    return render(request, 'companies/company_list.html', {'companies': companies})

def company_detail(request, company_id):
    company = get_object_or_404(Companies, pk=company_id)
    employees = Employees.objects.filter(company=company)
    return render(request, 'companies/company_detail.html', {'company': company, 'employees': employees})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CompanyForm()
    return render(request, 'companies/company_form.html', {'form': form})

def company_update(request, company_id):
    company = get_object_or_404(Companies, pk=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail', company_id=company.id)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'companies/company_form.html', {'form': form})

def company_delete(request, company_id):
    company = get_object_or_404(Companies, pk=company_id)
    if request.method == 'POST':
        company.delete()
        return redirect('index')
    return render(request, 'companies/company_confirm_delete.html', {'company': company})

#################################################### employee views

def employee_list(request):
    employees = Employees.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employees, pk=employee_id)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, employee_id):
    employee = get_object_or_404(Employees, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_delete(request, employee_id):
    employee = get_object_or_404(Employees, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})