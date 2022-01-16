from django.shortcuts import render
import interface

# Create your views here.
def index(request):
    return render(request, "index.html")

def map(request):
    if map.method == "POST":
        pickup = request.POST.get('pickup')
        destination = request.POST.get('dest')
        passengers = request.POST.get('passengers')
        pickup_lat, pickup_long = pickup.split(', ')
        dest_lat, dest_long = destination.split(', ')
        pr = interface.Predictor("model.pkl")
        pred = pr.predictCost(pickup_long, pickup_lat, dest_long, dest_lat, passengers)
    context = {
        'predictedcost':  '$ {}'.format(pred) # {{predictedcost}}
    }

    return render(request, "result.html", context) 
