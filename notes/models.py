from django.db import models

# Create your models here.
class Notes(models.Model):
    date=models.DateField()
    topic=models.TextField()
    notes=models.TextField()

    def __str__(self):
        return self.topic
