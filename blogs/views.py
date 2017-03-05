from django.shortcuts import render
from django.http import  HttpResponse
from . import models

def index(request):
    # pk 是Primary key主键的意思即为文章id
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})
# Create your views here.
