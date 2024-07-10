from django.db import models


# Create your models here.

class Credentials(models.Model):
    platform = models.TextField()
    username = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.platform
