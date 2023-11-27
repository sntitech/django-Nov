from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField()

class Task(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)






