import googlemaps, json, os, polyline, webbrowser
import addRouteToMap, pointsFunction, intersectionParse, pygmaps


kml_file = '/Users/cssummer16/Desktop/summer_2016/readme/python/KML/IntersectionPoints.kml'
# API key 
gmaps = googlemaps.Client(key='AIzaSyDaPfA_TUTlbHLDH0K48qS-Jh2ETfCTz_0')
text_file=pointsFunction.kmlParse(kml_file)
intersection = []
mapOfNodes = {}
intersection=intersectionParse.createIntersections(text_file)
directionIntersection = intersection

# The Map
THE_MAP = None
HTML_NAME = './dirProject.html'
LAT = 34.09668
LNG = -117.71978
MAP_ZOOM = 15

count = 0
def callDirections():
	start = [directionIntersection[count].latlng[1], directionIntersection[count].latlng[0]]
	end   = [34.10185, -117.71747]

	#making a call to the google maps api 
	dirs = gmaps.directions(start, end, "walking")
	# the points google returns from the direstions call
	points =dirs[0]["overview_polyline"]["points"]
	# the distance of the route will possibly be helpful in the future if I am changing the colors of the arrows 
	distance = dirs[0]["legs"][0]["distance"]["value"]
	addRouteToMap.addRoute(mapOfNodes,intersection, directionIntersection, points)



def updateMap(gmaps):
	global THE_MAP
	callDirections()
	THE_MAP = pygmaps.maps(LAT, LNG, MAP_ZOOM)
	dictKeys = dict.keys(mapOfNodes)
	for key in dictKeys:
		# print(key.value)
		if(mapOfNodes[key] != None):
			# print('here')
			THE_MAP.addpath([mapOfNodes[key], key], key.value)
	print('here2')
	THE_MAP.addpoint(34.10185, -117.71747, "#FF0000")

# the school **look into changing it into the school logo*** add polygone here ***
updateMap(HTML_NAME)

THE_MAP.draw(HTML_NAME)

