from datetime import datetime
from django.db import models

# Create your models here.

class Blog(models.Model):
    sno = models.CharField(max_length=50)
    author = models.CharField(max_length=50,default='shehbaz')
    title = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='static/images/')
    description = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    lang = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.title


    def showing_description(self):
        return self.description[:159]
    
    
class BlogComments(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=("Blog"), on_delete=models.CASCADE)
    comment = models.TextField()
    commentor = models.CharField(max_length=50)
    parent = models.ForeignKey('self', verbose_name=("Reply to"), on_delete=models.CASCADE, null= True)
    