import polyline, math
import intersectionParse, dirProject

THRESHOLD = .0001101
THRESHOLD = 0.0001

# school = intersectionParse.Node([-117.71747, 34.10185,]) 
def addRoute (intersection, directionIntersection, points):
    mapOfNodes = {}
    close_intersections = []
    school = intersectionParse.Node(-117.71747, 34.10185)
    previous_node = points[0]

    for point_node in points[1:]:
        if point_node in directionIntersection:
            directionIntersection.remove(point_node)
        #mapOfNodes[previous_node] = point_node
        # print("Point_node, and Previous_node:", point_node.lat, previous_node.lat)
        distance_lat = abs(point_node.lat - previous_node.lat)
        distance_lng = abs(point_node.lng - previous_node.lng)
        if  distance_lat >.00350 or distance_lng >.00350:
            radius = (point_node - previous_node)/2
            midpoint = intersectionParse.Node((min(point_node.lng, previous_node.lng) + distance_lng)/2, (min(point_node.lat, previous_node.lat) + distance_lat)/2)
            close_intersections = [inter for inter in intersection if inter - midpoint <= radius]
             
            # Find intersections that are within the radius at the midpoint of two points
            # Sort
            # find the distance using projection of a line 
        # print('here')

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

