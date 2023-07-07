from django.contrib import admin
from employee_app.models import Employee


@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display = ('name', 'id', 'email', 'department', 'position', 'job_role', 'status', 'avtar')

    search_fields = ('status', 'name', 'position', 'department')