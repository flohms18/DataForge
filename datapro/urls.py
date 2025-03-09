from django.urls import path

from . import views
from datapro.views import career_detail
from datapro.views import article_detail


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("career", views.career, name="career"),
    path("glossary", views.glossary, name="glossary"),
    path("governance", views.governance, name="governance"),
    path("career/<int:career_id>/", career_detail, name="career_detail"),
    path("article/<int:article_id>/", article_detail, name="article_detail"),

    
]
