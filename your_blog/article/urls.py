from django.urls import path
from . import views

# add this will give you a namespace for your urls within app
app_name = 'article'
urlpatterns = [
    path('article-list/', views.article_list, name="article_list"),
    path('article-detail/<int:pk>', views.article_detail, name="article_detail"),
]