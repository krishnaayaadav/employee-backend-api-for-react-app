
from django.urls import path
from employee_app.ApiFiles import api_views

urlpatterns = [
    path('employees/', api_views.EmployeeAPI.as_view()),
    path('employees/<int:empId>/', api_views.EmployeesAPI.as_view()),

]

