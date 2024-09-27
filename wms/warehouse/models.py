
from django.db import models
import uuid
# from django.core.mail import send_mail
# from django.dispatch import receiver
from django.db.models.signals import post_save

class Role(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('operator', 'Operator'),
    ]
    name = models.CharField(max_length=225, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('operator', 'Operator'),
    ]
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    capacity = models.IntegerField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User table

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


