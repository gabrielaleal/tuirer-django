from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    picture = models.ImageField('Foto de perfil', default='/img/blank-profile.png')
    following = models.ManyToManyField('self', blank=True)