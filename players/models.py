from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Player(models.Model):
    GENDER_CHOICES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=20, blank=True, default='')
    phone_number = models.CharField(max_length=15, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, default=None)
    web_site = models.CharField(max_length=400, blank=True, default='')
    account_holder = models.CharField(max_length=40, blank=True, default='')
    account_email = models.EmailField(max_length=254, blank=True, default='')

    coins = models.BigIntegerField(default=0, validators=[
                MaxValueValidator(5),
                MinValueValidator(0),
                ])
    lives = models.IntegerField(default=0, validators=[
                MaxValueValidator(5),
                MinValueValidator(0),
                ])
    rematchs = models.IntegerField(default=0, validators=[
                MaxValueValidator(5),
                MinValueValidator(0),
                ])
