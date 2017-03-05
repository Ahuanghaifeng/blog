from django.shortcuts import render
from django.http import  HttpResponse
from . import models

def index(request):
    # pk 是Primary key主键的意思即为文章id
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index.html', {'article':article})
# Create your views here.
