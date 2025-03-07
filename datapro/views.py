from django.shortcuts import render, get_object_or_404

from .models import DataCareer


def career(request):
    queryset = DataCareer.objects.all()  
    return render(request, "datapro/career.html",{'queryset': queryset})

def about(request):
    return render(request,'datapro/about.html')

def index(request):
    return render(request,'datapro/index.html')

def governance(request):
    return render(request,'datapro/governance.html')

def career_detail(request, career_id):
    career = get_object_or_404(DataCareer, id=career_id)    
    obj = DataCareer.objects.all()
    return render(request, "datapro/career_detail.html", {
        'career': career, 
        'obj': obj
    })

def article(request):
    return render(request,'datapro/article.html')