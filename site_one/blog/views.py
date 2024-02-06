from django.shortcuts import render
from .models import Article
# Create your views here.

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'blog/year_archive.html', context)
def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month': month, 'article_list': a_list}
    return render(request, 'blog/month_archive.html', context)

def article_detail(request, year, month, pk):
    article = Article.objects.get(pub_date__year=year, pub_date__month=month, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

def home(request):
    return render(request, 'base.html', {'name': 'Django'})
