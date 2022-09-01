from django.shortcuts import render
from melons.models import Article

def main(request):

    article1 = Article.objects.all()[len(Article.objects.all())-1]
    article2 = Article.objects.all()[len(Article.objects.all())-2]
    article3 = Article.objects.all()[len(Article.objects.all())-3]
    context = {
        'article1': article1,
        'article2': article2,
        'article3': article3,
    }
    return render(request, 'apples/main.html', context)