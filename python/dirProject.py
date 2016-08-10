#!/usr/bin/env python3

import googlemaps, json, os, polyline, webbrowser, time, copy
import addRouteToMap, pointsFunction, intersectionParse, pygmaps
import argparse


# The Map
THE_MAP = None
LAT = 34.09668
LNG = -117.71978
MAP_ZOOM = 15
THE_MAP = pygmaps.maps(LAT, LNG, MAP_ZOOM)

def main(kml_file, html_file, text_file):
    # API key 
    gmaps = googlemaps.Client(key='AIzaSyDaPfA_TUTlbHLDH0K48qS-Jh2ETfCTz_0')
    #for debugging
    colors = ['#000000','#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']
    intersection_file = pointsFunction.kmlParse(kml_file,text_file)
    intersections=intersectionParse.createIntersections(intersection_file)

    mapOfNodes = {}
    # directionIntersections = intersections
    directionIntersections = copy.deepcopy(intersections)
    i = 0
    # the school **look into changing it into the school logo*** add polygone here ***

    while(directionIntersections):
        temp_node = directionIntersections.pop()
        start = [temp_node.lng, temp_node.lat]
        
        end   = [34.10185, -117.71747]

        #making a call to the google maps api
        dirs = gmaps.directions(start, end, "walking")
        #points = dirs[0]["overview_polyline"]["points"]

        points = [intersectionParse.Node(lng, lat) for lat, lng in polyline.decode(dirs[0]["overview_polyline"]["points"])]
        # the distance of the route will possibly be helpful in the future if I am changing the colors of the arrows
        points = addRouteToMap.snapToIntersection(points, intersections)

        mapOfNodes = addRouteToMap.addRoute(mapOfNodes, intersections, directionIntersections, points)

        i += 1
        if i >20: 
            # time.sleep(.5)
            i =0
            break
    color_count = 0
    for key in mapOfNodes:
        if(mapOfNodes[key] is not None):
            print("Map leg: ", mapOfNodes[key], key)
            print(key.lat, key.lng)
            print(mapOfNodes[key].lat, mapOfNodes[key].lng)
            THE_MAP.addpath([key, mapOfNodes[key]], key.value, colors[color_count])
            # THE_MAP.addpath([mapOfNodes[key], key], key.value, colors[color_count])
            color_count +=1
            if color_count == 6:
                color_count = 0

            
    THE_MAP.addpoint(34.10185, -117.71747, "#FF0000")

    THE_MAP.draw(html_file)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--kml','-k', metavar='FILE', type=argparse.FileType('r'),
                        required=True,
                   help='Read intersections from kml FILE')
    parser.add_argument('--html','-m', metavar='FILE', type=argparse.FileType('w'),
                        required=True,
                        help='Write the output to html FILE')
    parser.add_argument('--text','-t', metavar='FILE', type=argparse.FileType('w'),
                        required=True,
                        help='Write the text version of the coordinates to FILE')

    args = parser.parse_args()
    main(args.kml, args.html, args.text)
