from django.shortcuts import render
from blog.models import Post
from recomend.models import Attraction

# Create your views here.

def index(request):
    post = Post.objects.get(pk=1)
    attraction = Attraction.objects.all()
    return render(
        request, 
        "single/index.html",
        {
            "attr" : attraction,
            "popo" : post,
        }
        )



