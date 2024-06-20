from django.shortcuts import render

# Create your views here.

def map (request):
    # pkl = ParkingLot.objects.all().order_by('pk')
    return render(
        request,
        'map_test/map_test.html',

        # {
        #     'pkl': pkl,
        # }
    )

def time (request):
    return render(
        request,
        'map_test/walk_time.html'
    )

def graph (request):
    return render(
        request,
        'map_test/graph.html'
    )
    
def overlay (request):
    return render(
        request,
        'map_test/overlay.html'
)
    
def select (request):
    return render(
        request,
        'map_test/select.html'
    )


