from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class employeestatus(models.Model):
    EMPLOYEE = "Employee"
    BOSS = "Boss"
    role_CHOICES = [
        (EMPLOYEE, 'Employee'),
        (BOSS, 'Boss'),

    ]
    role = models.CharField(
        max_length=10,
        choices=role_CHOICES,
        default= EMPLOYEE
    )

    profileimage = models.ImageField(null = True, blank= True, upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leaves = models.IntegerField(null = True, default = 14)

    def __str__(self):
        return f"{self.user} is a {self.role}"

class task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    duedate = models.DateField(default=0)
    users = models.ManyToManyField(User)
    leaves = models.IntegerField(default= 14)
    INCOMPLETE = "Incomplete"
    COMPLETE = "Complete"
    role_CHOICES = [
        (INCOMPLETE, 'Incomplete'),
        (COMPLETE, 'Complete'),
    ]
    status = models.CharField(
        max_length=10,
        choices=role_CHOICES,
        default= INCOMPLETE
    )
    def __str__(self):
        return f"{self.title} is due on {self.duedate}"
    def serialize(self):
        return {
            "title": self.title,
            "duedate": self.duedate,
        }

class todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todoitem = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.user} needs to do {self.todoitem}"

class leaves(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leavedate = models.DateField(default=0)
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    TAKEN = "TAKEN"
    role_CHOICES = [
        (PENDING, 'PENDING'),
        (APPROVED, 'APPROVED'),
        (TAKEN, "TAKEN" ),
    ]
    status = models.CharField(
        max_length=10,
        choices=role_CHOICES,
        default= PENDING
    )
    def serialize(self):
        return {
            "user": self.user,
            "leavedate": self.leavedate,
            "status": self.status
        }
    def __str__(self):
        return f"{self.user} applied leave on {self.leavedate}"
   