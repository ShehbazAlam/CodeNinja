from django.http import HttpResponse
from django.shortcuts import render

from home.models import About, Services, Social, Testimonials

# Create your views here.
def index(request):
    about = About.objects.all()
    service = Services.objects.all()
    social = Social.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request,'index.html',{'about':about,'services':service ,'social': social, 'testimonials':testimonials})