from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from projects.models import Project, ProjectComments

# Create your views here.
def projectindex(request):
    projects = Project.objects.all()
    return render(request,'projectindex.html',{'projects':projects})

def project(request , project_title):
    projectDetails = get_object_or_404(Project, title=project_title)
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('comment'):
            
            pcomment = ProjectComments()
            pcomment.commentor = request.POST.get('name')
            pcomment.comment = request.POST.get('comment')
            pcomment.project = projectDetails.id
            pcomment.save()
        
            message = 'comment added sucessfully'
            return render(request, 'project.html',{'message': message})
            
        else:
            message = 'Name or comment could not be empty'
            return render(request, 'project.html',{'message': message})
    return render(request, 'project.html',{'projectDetail':projectDetails})

def search(request):
    if request.method=="GET":
        search_res = request.GET.get('querry')
        project = Project.objects.filter(title__icontains=search_res)
        return render(request, 'searchproject.html',{'result':project})
        