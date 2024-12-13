from django.db import models

# Create your models here.
class Article(models.Model):
    task=models.CharField(max_length=200)
    detail=models.TextField()

    def register(self):
        self.save()

    def __str__(self):
        return self.task