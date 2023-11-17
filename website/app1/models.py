from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, default="")
    
class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)