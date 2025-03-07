from django.urls import path

from . import views
from datapro.views import career_detail

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("career", views.career, name="career"),
    path("governance", views.governance, name="governance"),
    path("career/<int:career_id>/", career_detail, name="career_detail"),
    path("article", views.article, name="article")
    
]
