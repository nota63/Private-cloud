from django.db import models

# Create your models here.

class Contacts(models.Model):
    name=models.CharField(max_length=244)
    relation=models.CharField(max_length=200)
    contact_number=models.TextField()

    def __str__(self):
        return f"private contact from {self.name}"