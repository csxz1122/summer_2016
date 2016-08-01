#!/usr/bin/env python3

import googlemaps, json, os, polyline, webbrowser
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
    intersection_file = pointsFunction.kmlParse(kml_file,text_file)
    intersection=intersectionParse.createIntersections(intersection_file)

    directionIntersection = intersection

    # the school **look into changing it into the school logo*** add polygone here ***

    start = [directionIntersection[0].lng, directionIntersection[0].lat]
    end   = [34.10185, -117.71747]

    #making a call to the google maps api
    dirs = gmaps.directions(start, end, "walking")
    #points = dirs[0]["overview_polyline"]["points"]

    points = [intersectionParse.Node(lng, lat) for lat, lng in polyline.decode(dirs[0]["overview_polyline"]["points"])]
    # the distance of the route will possibly be helpful in the future if I am changing the colors of the arrows
    
    points = addRouteToMap.snapToIntersection(points, intersection)

    mapOfNodes = addRouteToMap.addRoute(intersection, directionIntersection, points)
    
    for key in mapOfNodes:
        if(mapOfNodes[key] is not None):
            print("Map leg: ", mapOfNodes[key], key)
            #THE_MAP.addpath([key, mapOfNodes[key]], key.value)
            THE_MAP.addpath([mapOfNodes[key], key], key.value)
            
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
