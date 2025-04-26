from django.shortcuts import render

from .models import Article


def home_view(request):
    """
    Renders the homepage with the 5 most recent blog posts.
    """
    article = Article.objects.order_by("-id")[:5]
    return render(request, "home.html", {"article": Article})



def article_list_view(request):
    """
    Display the full list of blog posts.
    """
    article = Article.objects.all()
    context = {"article": article}
    return render(request, "article_list.html", context)