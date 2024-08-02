from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    address = models. TextField()
    emp_id = models.IntegerField()
    salary = models.FloatField()
    active_emp = models.BooleanField(default=True)
    joined_date = models.DateField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.name
