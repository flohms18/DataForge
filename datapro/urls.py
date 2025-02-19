from django.urls import path

from . import views

urlpatterns = [
    path("james", views.index, name="index"),
    path("", views.DataProDetail, name="DataProfessionDetail"),
]