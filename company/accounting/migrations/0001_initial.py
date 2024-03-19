# Generated by Django 5.0.3 on 2024-03-19 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.department')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='salaryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.salary'),
        ),
    ]
