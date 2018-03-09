from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


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
    # Se queda pendiente
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
    # Referencia al modelo, entre comilla simples 'players.player'
    follow = models.ManyToManyField('players.player', related_name='followers')

    @classmethod
    def following(self, me_id, follow_id):
        if not me_id == follow_id:
            me = self.objects.get(pk=me_id)
            player = self.objects.get(pk=follow_id)
            me.follow.add(player)
            me.save()
        else:
            pass
