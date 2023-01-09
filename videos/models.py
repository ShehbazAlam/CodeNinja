from django.db import models
from datetime import datetime

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='static/images/')
    description = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    lang = models.TextField(default='other')
    link = models.TextField(max_length=300,default='https://youtube.com')
    
    def __str__(self):
        return self.title
