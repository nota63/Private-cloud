from django.db import models


# Create your models here.

class Tasks(models.Model):
    task = models.TextField()
    time = models.TextField()
    date = models.TextField()
    description = models.TextField()
    select = models.TextField()

    def __str__(self):
        return self.task
