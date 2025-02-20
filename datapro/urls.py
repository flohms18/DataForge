from django.urls import path

from . import views

urlpatterns = [
    path("<int:DataPro_id>/", views.detail, name="detail"),]