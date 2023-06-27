from django.db import models

# Create your models here.
class Employees(models.Model):
    Ename=models.CharField(max_length=100)
    Eid=models.IntegerField(primary_key=True)
    Eage=models.IntegerField()