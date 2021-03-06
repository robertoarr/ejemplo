from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateField(null=False)
    phone_number = models.CharField(max_length=15, null=False, default='', blank=True)
    postal_code = models.IntegerField(null=False)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    office = models.ForeignKey('users.Office', related_name='employee', on_delete=models.SET_NULL, null=True)
    reports_to = models.ForeignKey('users.Employee',
                                   related_name='in_charge_of',
                                   on_delete=models.SET_NULL,
                                   null=True)
    extension = models.IntegerField(null=False, default=0000)
    job_tittle = models.CharField(max_length=20, null=False)


class Office(models.Model):
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    postal_code = models.IntegerField(null=False)


class Payment(models.Model):
    customer = models.ForeignKey('users.Customer', related_name='payment', on_delete=models.CASCADE, null=True)
    payment_date = models.DateTimeField(editable=False, auto_now=True)
    amount = models.IntegerField(null=False)
