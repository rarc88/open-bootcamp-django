from django.shortcuts import render
from .forms import EmployeeForm


def form(req):
    employee_form = EmployeeForm()
    return render(req, 'form.html', {'employee_form': employee_form})
