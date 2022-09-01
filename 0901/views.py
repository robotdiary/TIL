from tkinter.tix import Form
from django.shortcuts import render, redirect
from .models import Article


def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'melons/articles.html', context)

def new(request):
    return render(request, 'melons/new.html')

def create(request):
    person = request.GET.get('person')
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article(person=person, title=title, content=content)
    article.save()
    return redirect('melons:articles')

def details(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'melons/details.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('melons:articles')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'melons/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('melons:details', article.pk)