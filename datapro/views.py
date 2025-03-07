from django.shortcuts import render

from .models import DataCareer


def index(request):
    return render(request, "datapro/index.html")

def about(request):
    return render(request,'datapro/about.html')

def career(request):
    return render(request,'datapro/career.html')