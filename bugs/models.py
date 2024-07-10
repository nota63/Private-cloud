from django.db import models


class Bugs(models.Model):
    name = models.TextField()
    username=models.TextField()
    section=models.TextField()
    issue=models.TextField()
    email=models.TextField()
    date=models.DateField()

    def __str__(self):
        return f"Bug fix request from {self.name}"