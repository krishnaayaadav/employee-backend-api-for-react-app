import random
from employee_app.models import Employee
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# employee status here
EMPLOYEE_STATUS = ('Active', 'Awaiting', 'Pending', 'Onboarding')

# singal to add employee status when emp obj is created
@receiver(post_save, sender=Employee)
def employees_status_adder(sender, instance, created, *args,  **kwargs):
    if created:
       instance.status = random.choice(EMPLOYEE_STATUS)
       instance.save()