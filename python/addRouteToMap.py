import polyline
import intersectionParse 
#if a break was called
# using so that I can tell when the path has finished if the inter.value > 0 
# school = intersectionParse.Node([-117.71747, 34.10185,]) 
# Currently dealing with the information given from google maps
def addRoute (mapOfNodes, intersection, directionIntersection, points):
	school = intersectionParse.Node([-117.71747, 34.10185,])
	#previous_node is only this value until
	previous_node = intersectionParse.Node([-117.71747, 34.10185,]) 

	for point in polyline.decode(points):
		point_node = intersectionParse.Node([point[1],point[0]])
		result = interExist(point, intersection)
		if(result == False):
			result = point_node
		else:
			directionIntersection.remove(result)
	
		if(result in mapOfNodes):
			print('not done yet')
			break 
		else:
			mapOfNodes[result] = previous_node
			previous_node = point_node
	return mapOfNodes
def interExist(point, intersection):
	for inter in intersection:
			# does there exist a node in iter that is close to the point
			if(abs(point[0] - float(inter.latlng[1])) <.0001101 and abs(point[1] - float(inter.latlng[0])) <.0001101):
				return inter
	return False
