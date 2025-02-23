from django.http import HttpResponse
from django.shortcuts import render

from .models import DataJob


def index(request):
    queryset = DataJob.objects.all()  
    return render(request, "datapro/index.html",{'queryset': queryset})

def governance(request):
    return render(request, "datapro/governance.html")