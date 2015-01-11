from django.db import models
from datetime import datetime
class Gif(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, default=datetime.now())
    pub_date.editable = True
    title = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.title

# Create your models here.
