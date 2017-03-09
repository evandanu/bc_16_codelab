from urlib.request import urlopen

import json

def know_distance():
	distance_url="https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyDGaCLRyVSyqbqyMJ6KOtKPjJWQB4wyn4I"
	request=urlopen(distance_url)
	read=request.read().decode("utf")
	json_object=json.loads(read)
	print(json.dumps(json_object))

know_distance()


