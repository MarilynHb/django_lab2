from django.shortcuts import redirect, render
from .models import Department, Employee

#region Department
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def delete_department(request, department_id):
    Department.objects.get(id=department_id).delete()
    return redirect('department_list')

def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('name')
        if department_name:
            Department.objects.create(name=department_name)
            return redirect('department_list')
    return render(request, 'add_department.html')

def edit_department(request, department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        department_name = request.POST.get('name')
        if department_name:
            department.name = department_name
            department.save()
            return redirect('department_list')
    return render(request, 'edit_department.html', {'department': department})
#endregion

#region Employee
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('employee_list')

def add_employee(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        employee_name = request.POST.get('name')
        dob = request.POST.get('dob')
        department_id = int(request.POST.get('department'))
        department = Department.objects.get(id=department_id)
        if employee_name and dob and department:
            Employee.objects.create(name=employee_name, dob=dob, department_id=department)
            return redirect('employee_list')
    return render(request, 'add_employee.html', {'departments': departments})

def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    departments = Department.objects.all()
    if request.method == 'POST':
        employee_name = request.POST.get('name')
        dob = request.POST.get('dob')
        department_id = int(request.POST.get('department'))
        department = Department.objects.get(id=department_id)
        if employee_name and dob and department:
            employee.name = employee_name
            employee.dob = dob
            employee.department_id = department
            employee.save()
            return redirect('employee_list')
    return render(request, 'edit_employee.html', {'employee': employee, 'departments': departments})

#endregion