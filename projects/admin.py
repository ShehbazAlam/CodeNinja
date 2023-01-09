from django.contrib import admin

from projects.models import Project, ProjectComments

# Register your models here.
admin.site.register(ProjectComments)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)