from django.db import models


# Create your models here.

class Address(models.Model):
    name = models.TextField()
    city=models.TextField()
    pin_code=models.TextField()
    colony=models.TextField()
    house_number=models.TextField()
    district=models.TextField()
    state=models.TextField()
    country=models.TextField()

    def __str__(self):
        return f"private address of {self.name}"
