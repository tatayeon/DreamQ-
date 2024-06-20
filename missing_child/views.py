from django.shortcuts import render
from .models import Post 

# Create your views here.

def mia (request):
    post = Post.objects.all().order_by('pk')
    return render(
        request,
        'missing_child/children_list.html',
        {
            'ps': post,
        }
    )

def mia_info (request, pk):
    detail = Post.objects.get(pk=pk)

    return render(
        request,
        'missing_child/child_info.html',
        {
            'detail': detail,
        }
    )
    