from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("governance", views.governance, name="governance"),
    path("about", views.about, name="about")

]
