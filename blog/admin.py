from django.contrib import admin

from blog.models import Blog, BlogComments

# Register your models here.

admin.site.register(BlogComments)
@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)