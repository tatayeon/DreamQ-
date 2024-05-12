from django.shortcuts import render
from recomend.models import Attraction

def search(request):
    if request.method == 'POST':
        searched = request.POST['Search']        
        attraction = Attraction.objects.filter(title=searched)
        return render(request, 'single/index.html', {'searched': searched, 'attraction': attraction})
    else:
        return render(request, 'single/index.html', {}) 