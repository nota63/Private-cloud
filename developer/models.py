from django.db import models


# Create your models here.

class Developer(models.Model):
    title = models.TextField()
    description = models.TextField()
    python_version = models.TextField()
    required_libraries = models.TextField()
    code = models.TextField()

    def __str__(self):
        return self.title
