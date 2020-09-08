from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ArticleCategory(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)
     
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

class ArticlePost(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        ArticleCategory,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )

    def __str__(self):
        return self.title
