from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # email = models.EmailField(max_length=250)

    def __str__(self):
        return self.username
