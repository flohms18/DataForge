from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import DataCareer, Article, GlossaryTerm


def career(request):
    queryset = DataCareer.objects.all()  
    return render(request, "datapro/career.html",{'queryset': queryset})

def about(request):
    return render(request,'datapro/about.html')

def glossary(request):
    glossary_dict = {}
    terms = GlossaryTerm.objects.all().order_by("term")
    for term in terms:
        FirstLetter = term.term[0].upper()
        if FirstLetter not in glossary_dict:
            glossary_dict[FirstLetter] = []
        glossary_dict[FirstLetter].append(term)

    return render(request, 'datapro/glossary.html', {
        'glossary_dict': glossary_dict})

def index(request):
    obj = Article.objects.all().order_by('-is_featured')
    paginator = Paginator(obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "datapro/index.html", {
        'obj': obj,
        'page_obj' : page_obj,
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