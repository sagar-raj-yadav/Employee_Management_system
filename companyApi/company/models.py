from django.db import models

# Create company model

class companyModel(models.Model):
    company_id=models.AutoField(primary_key=True) #company_id is my primary key
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    about=models.CharField(max_length=200)
    type=models.CharField(max_length=200,choices=(('IT','IT'),('NON IT','NON IT'),('PHONES','PHONES')) )
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

# Create employee model
class EmployeeModel(models.Model):
    employee_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone= models.CharField(max_length=15)
    