from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ArticlePost

# Create your views here.
def helloDjango(request):
    return render(request, 'base.html')

def article_list(request):
    article_list = ArticlePost.objects.all()
    context = {'articles': article_list}
    return render(request, 'article/list.html', context)


def article_detail(request, pk):
    article = get_object_or_404(ArticlePost, pk=pk) # ArticlePost.objects.get(pk=id)

    context = {'article': article }
    return render(request, 'article/detail.html', context)