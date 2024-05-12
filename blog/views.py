from django.shortcuts import render
from .models import Post
from .models import comment
# Create your views here.

def index(request):
    posts = Post.objects.all()

    return render(
        request, 
        "blog/index.html",{
            "post" : posts
        }
        )

def singpage(requst, pk):
    P11 = Post.objects.get(pk=pk)
    p22 = comment.objects.all()
    return render(
        requst,
        "blog/sing_page.html",
        {
            "pone" : P11,
            "ptow" : p22
        }

    )
