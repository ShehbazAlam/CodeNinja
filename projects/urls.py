from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.projectindex, name='Project Home'),   
    path('view/<str:project_title>/',views.project, name='details'), 
    path('search/',views.search, name="search"),
    path('comment/',views.pcomment, name="pcomment"),
    
]