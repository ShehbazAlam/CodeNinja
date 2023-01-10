from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
        
def comment(request):
    pro = request.POST.get('blog')
    if request.method == "POST":
                
        commentor = request.POST.get('comentor')
        comment = request.POST.get('comment')
        blog = request.POST.get('blog')
        cBlog = Blog.objects.get(title=blog)
        pcomment = BlogComments(Blog=cBlog, comment=comment, commentor=commentor)
        pcomment.save()

        messages.success(request,'comment added sucessfully')
        
    return redirect(f"/Blogs/view/{pro}")