from django.shortcuts import render

from .models import DataCareer


def career(request):
    queryset = DataCareer.objects.all()  
    return render(request, "datapro/career.html",{'queryset': queryset})

def about(request):
    return render(request,'datapro/about.html')

def index(request):
    return render(request,'datapro/index.html')