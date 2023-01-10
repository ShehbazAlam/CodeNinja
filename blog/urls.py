from . import views
from django.urls import path

urlpatterns = [
    path('',views.blogindex, name='Blog Home'), 
    path('read/<str:blog_title>/', views.details, name="bdetails"),
    path('search/',views.search, name="bsearch"),
    path('comment/',views.comment, name="bcomment"),
]