from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default='Rakib')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ExtendUser(AbstractUser):
    email = models.EmailField(max_length=50, blank=False, verbose_name='email')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = "email"
