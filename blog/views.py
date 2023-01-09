from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog, BlogComments

# Create your views here.

def blogindex(request):
    blogs = Blog.objects.all()
    return render(request,'blogindex.html',{'blogs':blogs})

def details(request, blog_title):

        
    blog_details = get_object_or_404(Blog, title=blog_title)
    comments = BlogComments.objects.filter(blog = blog_details.id)
    return render(request, "blog.html", {'blog_details': blog_details, 'comments': comments})

def search(request):
    if request.method=="GET":
        search_res = request.GET.get('querry')
        blog = Blog.objects.filter(title__icontains=search_res)
        return render(request, 'searchblog.html',{'result':blog})
        