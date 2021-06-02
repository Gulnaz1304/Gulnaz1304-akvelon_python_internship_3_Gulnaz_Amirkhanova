from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractBaseUser):
    """model for user"""
    first_name = models.CharField('first name', max_length=150)
    last_name = models.CharField('last name', max_length=150)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = "email"  # AbstractBaseUser requires username field


class Transaction(models.Model):
    """model for transaction"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")  # Each transaction is related
    amount = models.IntegerField()                                                         # to one user
    date = models.DateField(auto_now=True)

