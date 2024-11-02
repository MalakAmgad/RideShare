from django.shortcuts import render
import pickle
import math

# Load your trained model
with open('./savedmodel/mymodel.pkl', 'rb') as file:
    model = pickle.load(file)

def haversine(lat1, lon1, lat2, lon2):
    R = 3960  # Radius of the Earth in miles
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = (math.sin(dLat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dLon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # Distance in miles

def deploy(request):
    output_result = None
    
    # Define airport coordinates
    airports = {
        'JFK': (40.6413, -73.7781),
        'EWR': (40.6895, -74.1745),
        'LGA': (40.7769, -73.8740),
        'SOL': (40.5714, -74.7397)
    }
    
    if request.method == "POST":
        try:
            pickup_latitude = float(request.POST['pickup_latitude'])
            pickup_longitude = float(request.POST['pickup_longitude'])
            dropoff_latitude = float(request.POST['dropoff_latitude'])
            dropoff_longitude = float(request.POST['dropoff_longitude'])
            passenger_count = int(request.POST['passenger_count'])
            hour = int(request.POST['hour'])
            weekday = int(request.POST['weekday'])
            year = int(request.POST['year'])
            distance = float(request.POST['distance'])
            bearing = float(request.POST['bearing'])
            
            weather = 1 if request.POST['weather'] == "1" else 0
            traffic = 1 if request.POST['traffic'] == "1" else 0
            
            # Calculate distances to the airports
            jfk_dist = haversine(pickup_latitude, pickup_longitude, airports['JFK'][0], airports['JFK'][1])
            ewr_dist = haversine(pickup_latitude, pickup_longitude, airports['EWR'][0], airports['EWR'][1])
            lga_dist = haversine(pickup_latitude, pickup_longitude, airports['LGA'][0], airports['LGA'][1])
            sol_dist = haversine(pickup_latitude, pickup_longitude, airports['SOL'][0], airports['SOL'][1])

            input_data = [[pickup_longitude, dropoff_longitude, dropoff_latitude, passenger_count, hour, weekday,
                            year, jfk_dist, ewr_dist, lga_dist, sol_dist, distance, bearing, weather, traffic]]
            
            output_result = model.predict(input_data)[0]
        
        except Exception as e:
            output_result = f"Error: {str(e)}"

    return render(request, "main.html", {'output_result': output_result})
