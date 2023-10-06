from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return "%s" %(self.name)


class Employee(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    # department=models.CharField(max_length=20)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" %(self.emp_id, self.name)
    
