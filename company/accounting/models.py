from django.db import models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary_id = models.ForeignKey('Salary', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Salary(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.amount