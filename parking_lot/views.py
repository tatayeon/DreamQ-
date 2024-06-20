from django.shortcuts import render
from .models import ParkingLot

# Create your views here.

def parking (request):
    pkl = ParkingLot.objects.all().order_by('pk')
    return render(
        request,
        'parking_lot/pk_main.html',
        {
            'pkl': pkl,
        }
    )

def congestion (request, pk):
    cng = ParkingLot.objects.get(pk=pk)

    return render(
        request,
        'parking_lot/pk_congestion.html',
        {
            'cng': cng,
        }
    )
    