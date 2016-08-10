import googlemaps, json, os, polyline

def isochroneFunction(lat, lng, distance):
	gmaps = googlemaps.Client(key='AIzaSyDaPfA_TUTlbHLDH0K48qS-Jh2ETfCTz_0')
	# One degree of lat/lng is equivilent to 70 miles
	addit = (1*distance)/70 
	addit = addit/20
	pointOfDistance = []
	count = 0 
	tempLat = lat
	timeSeconds = [] 
	while count != 20:
		tempLat = tempLat + addit
		tempLng = lng
		pointOfDistance.append((tempLat, tempLng))
		count += 1 
	print(pointOfDistance)
	distanceMatrix = gmaps.distance_matrix(pointOfDistance, (lat, lng), "walking")
	print(distanceMatrix)
	for items in distanceMatrix['rows']:
		for element in items['elements']:
			timeSeconds.append(element['duration']['value'])

isochroneFunction(34.10185, -117.71747, 1)