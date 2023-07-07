from django.db import models


# Employees model here
class Employee(models.Model):
    name  = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=200)
    position   = models.CharField(max_length=200)
    job_role   = models.CharField(max_length=200)
    salary     = models.PositiveIntegerField()
    avtar      = models.ImageField(upload_to='Employees/Images')
    status     = models.CharField(blank=True, max_length=20)
