from django.contrib import admin

from videos.models import Video

# Register your models here.
@admin.register(Video)


class VideoAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)