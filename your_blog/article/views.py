from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloDjango(request):
    return render(request, 'base.html')
