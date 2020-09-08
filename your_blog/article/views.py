from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ArticlePost, ArticleCategory

# Create your views here.
def article_list(request):
    article_list = ArticlePost.objects.all()
    context = {'articles': article_list}
    return render(request, 'article/list.html', context)


def article_detail(request, pk):
    article = get_object_or_404(ArticlePost, pk=pk) # ArticlePost.objects.get(pk=id)

    context = {'article': article }
    return render(request, 'article/detail.html', context)

def article_categories(request):
    category_list = ArticleCategory.objects.all()
    article_list = ArticlePost.objects.all()
    category_post_count = {}
    for category in category_list:
        articles = article_list.filter(category__title__icontains=category)
        category_post_count[category.title]=len(articles)

    context = {'category_post_count': category_post_count}
    return render(request, 'article/categories.html', context)