from django.db import models

# Create your models here.
class employee_model(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
