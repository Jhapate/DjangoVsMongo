from django.db import models
from mongoengine import Document, fields

class Employees(models.Model):
    #field_Name = fields.StringField(required=True)
    #field_Name = fields.IntegerField(required=True)
    EmployeeId = models.AutoField(primery_key = True)
    first_name = models.CharField(max_length=30)
    Dept_name = models.CharField(max_length=20)
    


# Create your models here.
