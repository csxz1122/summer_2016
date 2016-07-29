import polyline
import intersectionParse 
#if a break was called
# using so that I can tell when the path has finished if the inter.value > 0 
# school = intersectionParse.Node([-117.71747, 34.10185,]) 
# Currently dealing with the information given from google maps
def addRoute (mapOfNodes, intersection, points):
	break_call = False
	school = intersectionParse.Node([-117.71747, 34.10185,])
	previous_node = intersectionParse.Node([-117.71747, 34.10185,])

	for point in polyline.decode(points):
		point_node = intersectionParse.Node([point[1],point[0]])
		result = interExist(point, intersection)
		if(result == False):
			if(point_node in mapOfNodes):
				print('not done yet')
				break 
			else:
				mapOfNodes[point_node] = previous_node
				previous_node = point_node
				print('I AM HERE WOWOWOWOWOWOWOWOWOWOW')
				print(point_node.latlng)
		else:
			# print(len(intersection))
			intersection.remove(result)
			# print(len(intersection))
			if(result in mapOfNodes):
				print('not done yet')
				break 
			else:
				mapOfNodes[result] = previous_node
				print('result')
				print(result.latlng)
				previous_node = point_node
				print('previous_node')
				print(previous_node.latlng)
		# print(mapOfNodes)
		# print(interExist(point, [school]))
	return mapOfNodes
def interExist(point, intersection):
	for inter in intersection:
			# does there exist a node in iter that is close to the point
			if(abs(point[0] - float(inter.latlng[1])) <.0001101 and abs(point[1] - float(inter.latlng[0])) <.0001101):
				print('point')
				print(point)
				print('inter')
				inter.latlng[0] = round(float(inter.latlng[0]), 5)
				inter.latlng[1] = round(float(inter.latlng[1]), 5)
				print(round(float(inter.latlng[0]), 5))
				return inter
	return False
