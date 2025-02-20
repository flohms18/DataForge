from django.http import HttpResponse
from django.shortcuts import render

from .models import DataProfession


def index(request):
    DataProList = DataProfession.objects
    context = {"DataProList": DataProList}
    return render(request, "datapro/index.html",context)
