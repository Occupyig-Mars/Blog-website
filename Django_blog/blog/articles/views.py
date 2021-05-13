from django.db.models.fields import DateField
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    article = Article.objects.all().order_by()
    return render(request,'articles/article_list.html',{'articles':article})

def article_detail(request,slug):
   # return HttpResponse(slug)
   article=Article.objects.get(slug=slug)
   return render(request,'articles/article_detail.html',{'article':article})