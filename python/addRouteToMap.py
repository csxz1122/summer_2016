import polyline
import intersectionParse

THRESHOLD = .0001101
THRESHOLD = 0.0001

#if a break was called
# using so that I can tell when the path has finished if the inter.value > 0 
# school = intersectionParse.Node([-117.71747, 34.10185,]) 
# Currently dealing with the information given from google maps
def addRoute (intersection, directionIntersection, points):
    mapOfNodes = {}
    
    school = intersectionParse.Node(-117.71747, 34.10185)
    #previous_node is only this value until
    previous_node = intersectionParse.Node(-117.71747, 34.10185)
    previous_node = points[0]

    for point_node in points[1:]:
        if point_node in directionIntersection:
            directionIntersection.remove(point_node)
        #mapOfNodes[previous_node] = point_node
        mapOfNodes[point_node] = previous_node
        previous_node = point_node
    return mapOfNodes

def snapToIntersection(points, intersection):
    return [interExist(point, intersection) for point in points]

def interExist(point, intersection):
    distances = [(point-intersection_node, intersection_node) for intersection_node in intersection]
    distances.sort()

    best_distance, best_node = distances[0]
    
    if best_distance < THRESHOLD:
        return best_node
    else:
        return point
