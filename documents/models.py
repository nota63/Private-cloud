from django.db import models


# Create your models here.

class Documents(models.Model):
    name=models.TextField()
    documents=models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
