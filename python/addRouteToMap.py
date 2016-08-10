import polyline, math
import intersectionParse, dirProject

# THRESHOLD = .0001101
THRESHOLD = 0.0002

# school = intersectionParse.Node([-117.71747, 34.10185,]) 
def addRoute (mapOfNodes, intersections, directionIntersection, points):
    close_intersections = []
    missing_intersection = []
    school = intersectionParse.Node(-117.71747, 34.10185)
    previous_node = points[0]

    for point_node in points[1:]:
        if point_node in directionIntersection:
            directionIntersection.remove(point_node)

        #mapOfNodes[previous_node] = point_node
        if point_node in mapOfNodes:
            # Place holder for where there should already be direction to the school
            mapOfNodes[previous_node] = point_node
            print('here, place holder for nodes already in mapOfNodes')
            break 

        distance_lat = abs(point_node.lat - previous_node.lat)
        distance_lng = abs(point_node.lng - previous_node.lng)
        
        if  distance_lat >.00050 or distance_lng >.00050:
            radius = (point_node - previous_node)/2
            midpoint = intersectionParse.Node((min(point_node.lat, previous_node.lat) + distance_lat/2), (min(point_node.lng, previous_node.lng) + distance_lng/2))

            close_intersections = [inter for inter in intersections if (inter - midpoint) <= radius]
            missing_intersection = getSpPoint(point_node, previous_node, close_intersections)

            distances = [(previous_node-inter, inter) for inter in missing_intersection]

            distances.sort()

            for inter in distances:
                if inter[1] != previous_node:
                    mapOfNodes[previous_node] = inter[1]
                    previous_node = inter[1]
        if point_node != previous_node:
            mapOfNodes[previous_node] = point_node

        previous_node = point_node
    print("done with path")
    return mapOfNodes

def snapToIntersection(points, intersections):
    return [interExist(point, intersections) for point in points]

def interExist(point, intersections):
    distances = [(point-intersection_node, intersection_node) for intersection_node in intersections]

    distances.sort()
    best_distance, best_node = distances[0]
    
    if best_distance < THRESHOLD:
        print("node")
        return best_node
    else:
        print("point")
        return point

def getSpPoint(A,B,close_intersections):
    print("In get SP point")
    missing_intersection = []
    for C in close_intersections:
        x1 = A.lat
        y1 = A.lng
        x2 = B.lat
        y2 = B.lng
        x3 = C.lat
        y3 = C.lng
        px = x2-x1
        py = y2-y1 
        dAB = px*px + py*py
        u = ((x3 - x1) * px + (y3 -y1) * py) /dAB
        x = x1 +u * px
        y = y1 + u * py 

        currNode = intersectionParse.Node(x,y)
        
        if currNode - C < THRESHOLD:
            missing_intersection.append(currNode)
    return missing_intersection





