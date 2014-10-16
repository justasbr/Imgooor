from django.db import models

class Gif(models.Model):
    title = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.title

# Create your models here.
