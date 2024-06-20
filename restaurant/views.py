from django.shortcuts import render
from .models import Post
from .models import Restaurant
# from .models import Restaurant

# Create your views here.

def rest (request):
    rest =Restaurant.objects.all().order_by('pk')
    return render(
        request,
        'restaurant/rest_main.html',
        {
            'rest': rest,
        }
    )

def rest_detail (request, pk):
    detail = Restaurant.objects.get(pk=pk)

    return render(
        request,
        'restaurant/rest_detail.html',
        {
            'detail': detail,
        }
    )
    
