from django.shortcuts import redirect, render
from .models import Department

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