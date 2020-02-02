from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120, help_text='Post Title')
    message = models.TextField(help_text='Say what you want')

    def __str__(self):
        return self.title
