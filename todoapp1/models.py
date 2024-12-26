from django.db import models

# Create your models here.
class Article(models.Model):
    date = models.DateField()
    task=models.CharField(max_length=200)
    priority = models.IntegerField() 
    detail=models.TextField()

    def register(self):
        self.save()

    def __str__(self):
        return f"{self.date}: {self.task} (Priority: {self.priority})"