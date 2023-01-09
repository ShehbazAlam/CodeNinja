from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from videos.models import Video
from django.db.models import Q

# Create your views here.
def videoindex(request):
    videos = Video.objects.all()
    return render(request,'videoindex.html',{'videos':videos})

def details(request,video_title):
    video_details = get_object_or_404(Video, title=video_title)
    relvideo = Video.objects.filter(lang = video_details.lang)
    recentvideo = Video.objects.all().order_by('-id')[:10]
    return render(request, "video.html", {'video_details': video_details, 'relvideo': relvideo, 'recentvideo': recentvideo })

def search(request):
    if request.method=="GET":
        search_res = request.GET.get('querry')
        video = Video.objects.filter(title__icontains=search_res)
        return render(request, 'searchvideo.html',{'result':video})
        
    
