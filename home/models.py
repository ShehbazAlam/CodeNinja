from django.db import models


# Create your models here.
class About(models.Model):
    description = models.TextField(blank=True)
    aboutimg = models.ImageField( upload_to='static/images')
    tags = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="static/images")
    
    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self):
        return self.name
    
class Social(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=150)
    icon = models.CharField(("fa fa-facebook"), max_length=50)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self):
        return self.name
    
class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(("image"), upload_to="static/images", height_field=None, width_field=None, max_length=None)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self):
        return self.name