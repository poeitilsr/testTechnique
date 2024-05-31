# companies/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.company_list, name="index"),
    path('<int:company_id>/', views.company_detail, name='company_detail'),
    path('new/', views.company_create, name='company_create'),
    path('<int:company_id>/edit/', views.company_update, name='company_update'),
    path('<int:company_id>/delete/', views.company_delete, name='company_delete'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/new/', views.employee_create, name='employee_create'),
    path('employees/<int:employee_id>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),
]
