from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ArticlePost, ArticleCategory
from taggit.models import Tag

MAX_FONT_SIZE = 52
MIN_FONT_SIZE = 16
# Utils
def convert_num_to_font_size(max_num, num):
    return max((int)(num / max_num * MAX_FONT_SIZE), MIN_FONT_SIZE)

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

def article_tags(request):
    tags = Tag.objects.all()
    article_list = ArticlePost.objects.all()
    counts = {}
    max_s, min_s = 0,10
    for tag in tags:
        articles = article_list.filter(tags__name__in=[tag])
        num_article_in_tag = len(articles)
        if max_s < num_article_in_tag:
            max_s = num_article_in_tag
        if min_s > num_article_in_tag:
            min_s = num_article_in_tag
        counts[tag.name] = len(articles)
    
    font_size = {}
    for tag, num in counts.items():
        font_size[tag] = convert_num_to_font_size(max_s, num)
    context = {'tags': tags, 'font_size': font_size,}
    return render(request, 'article/tags.html', context)    