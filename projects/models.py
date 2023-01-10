from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='static/images/')
    description = models.TextField(blank=True)
    lang = models.TextField(default='other')
    downlink = models.CharField(blank=True, max_length=250)
    demolink = models.CharField(blank=True, max_length=250)
    tags = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.title


    def showing_description(self):
        return self.description[:159]
    
    
class ProjectComments(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField()
    commentor = models.CharField(max_length=50)
   
    def __str__(self):
       return self.commentor
   