from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()
    rollnumber = models.IntegerField(default=0)
    imageUrl = models.CharField(max_length=200, default="")

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()
    designation = models.CharField(max_length=50)
    teacherid = models.IntegerField(default=0)
