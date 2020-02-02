from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.user.username)}'


class Post(models.Model):
    title = models.CharField(max_length=120, help_text='Post Title')
    message = models.TextField(help_text='Say what you want')
    author = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
