from django.contrib import admin

from home.models import About,Services,Social,Testimonials

# Register your models here.
admin.site.register(Services)
admin.site.register(Social)
admin.site.register(Testimonials)

@admin.register(About)

class AboutAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)