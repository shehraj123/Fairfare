from django.shortcuts import render
import interface

# Create your views here.
def index(request):
    return render(request, "index.html")

def map(request):
    if request.method == "POST":
        pickup = request.POST.get('pickup')
        destination = request.POST.get('dropoff')
        passengers = request.POST.get('passcount')
        print(pickup)
        print(destination)
        print(passengers)
        l = ['', None]
        if pickup in l or passengers in l or destination in l:
            return render(request, "index.html")
        pickup_lat, pickup_long = pickup.split(',')
        pickup_lat = float(pickup_lat)
        pickup_long = float(pickup_long)
        dest_lat, dest_long = destination.split(',')
        dest_lat = float(dest_lat)
        dest_long = float(dest_long)
        passengers = int(passengers)
        pr = interface.Predictor()
        pred = pr.predictCost(pickup_long, pickup_lat, dest_long, dest_lat, passengers)
        pred = abs(round(pred, 2))*10
        context = {
        'predictedcost': pred  # {{predictedcost}}
        }

    return render(request, "result.html", context) 
