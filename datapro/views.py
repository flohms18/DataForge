from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import DataCareer, Article


def career(request):
    queryset = DataCareer.objects.all()  
    return render(request, "datapro/career.html",{'queryset': queryset})

def about(request):
    return render(request,'datapro/about.html')

def glossary(request):
    return render(request,'datapro/glossary.html')

def index(request):
    obj = Article.objects.all()
    paginator = Paginator(obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "datapro/index.html", {
        'obj': obj,
        'page_obj' : page_obj
    })


def governance(request):
    return render(request,'datapro/governance.html')

def career_detail(request, career_id):
    career = get_object_or_404(DataCareer, id=career_id)    
    obj = DataCareer.objects.all()
    return render(request, "datapro/career_detail.html", {
        'career': career, 
        'obj': obj
})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)    
    return render(request, "datapro/article_detail.html", {
        'article': article
})