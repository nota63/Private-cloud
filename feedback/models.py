from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    rating = models.CharField(max_length=50)
    comments = models.TextField()
    recommend = models.CharField(max_length=3)

    def __str__(self):
        return f"Feedback from {self.name}"