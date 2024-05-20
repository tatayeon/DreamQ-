from django.shortcuts import render
from .models import Attraction
# Create your views here.

def index(request):
    return render(
        request, 
        "recomend/index_re.html",
        
        )

def family(request):
    return render(
        request,
        "recomend/recomend_famliy.html"
    )

def couple(request):
    return render(
        request,
        "recomend/recomend_couple.html"
    )

def friend(request):
    return render(
        request,
        "recomend/recomend_friend.html"
    )

def detail(request, type):
    
    reco = Attraction.objects.filter(type = type).all()
    # type = Attraction.objects.filter(type = type)
    
    return render(
        request,
        "recomend/recomend_detail.html",{
            "reco" : reco,
            "type" : type
        }
    )



