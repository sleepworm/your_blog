from django.urls import path
from . import views

# add this will give you a namespace for your urls within app
app_name = 'article'
urlpatterns = [
    path('hello/', views.helloDjango, name="hello")
]