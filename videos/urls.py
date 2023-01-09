from . import views
from django.urls import path, re_path

urlpatterns = [
    path('',views.videoindex, name='Blog Home'),   
    path('watch/<str:video_title>/', views.details, name="vdetails"),
    path('search/',views.search, name="vsearch"),
]