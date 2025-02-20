from django.http import HttpResponse
from django.shortcuts import render

from .models import DataProfession


def index(request):
    queryset = DataProfession.objects.all()    
    return render(request, "datapro/index.html",{'queryset': queryset})
