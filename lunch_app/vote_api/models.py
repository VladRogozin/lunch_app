from django.db import models
from users.models import Employee
from lunch_api.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    point = models.IntegerField()

    def __str__(self):
        return f"Vote by {self.employee.user.username} for {self.menu}"
