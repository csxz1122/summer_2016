#!/usr/bin/env python3

import argparse
import math
from functools import total_ordering

@total_ordering
class Node():
    def __init__(self,  lat, lng):
        self.color = 'yellow'
        self.distance = 0
        self.lat = round(float(lat),5)
        self.lng = round(float(lng),5)
        self.value = 8

    def __eq__(self, other):
        return (self.lat == other.lat) and (self.lng == other.lng)
    def __lt__(self, other):
        if self.lat != other.lat: return self.lat < other.lat
        else: return self.lng < other.lng
    def __hash__(self): 
        return (self.lat,self.lng).__hash__()
    def __sub__(self, other):
#        print(this.lat, other.lat, this.lng, other.lng)
        
        d_lat = (self.lat - other.lat) ** 2
        d_lng = (self.lng - other.lng) ** 2
        return math.sqrt(d_lat + d_lng)
    def __deepcopy__(self, memo):
         return(Node(self.lat, self.lng))

def createIntersections(file):
    def createNode(line):
        # Drop the last element (why is this 0.0 there to begin with?)
        lat, lng = line.strip().split(',')[:-1]
        return Node(lat,lng)

    return list(map(createNode, open(file).readlines()))

    
