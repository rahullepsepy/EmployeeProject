from django.db import models

# Database schema
class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
