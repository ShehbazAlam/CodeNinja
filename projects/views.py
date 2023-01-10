from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from projects.models import Project, ProjectComments

# Create your views here.
def projectindex(request):
    projects = Project.objects.all()
    return render(request,'projectindex.html',{'projects':projects})

def project(request , project_title):
    projectDetails = get_object_or_404(Project, title=project_title)
    comments = ProjectComments.objects.filter(project = projectDetails.id)
    return render(request, 'project.html',{'projectDetail':projectDetails, 'comments':comments})

def search(request):
    if request.method=="GET":
        search_res = request.GET.get('querry')
        project = Project.objects.filter(title__icontains=search_res)
        return render(request, 'searchproject.html',{'result':project})
        
        
def pcomment(request):
    pro = request.POST.get('project')
    if request.method == "POST":
                
        commentor = request.POST.get('comentor')
        comment = request.POST.get('comment')
        project = request.POST.get('project')
        cproject = Project.objects.get(title=project)
        pcomment = ProjectComments(project=cproject, comment=comment, commentor=commentor)
        pcomment.save()

        messages.success(request,'comment added sucessfully')
        
    return redirect(f"/projects/view/{pro}")
