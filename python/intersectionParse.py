class Node():
	def __init__(self,  latlng):
		self.color = 'yellow'
		self.distance = 0
		self.latlng = latlng
		self.value = 8

def createIntersections(file):
	intersection = []
	intersectionsTxt = open(file)
	for line in intersectionsTxt:
		intersection.append(line)

	for i,intersec in enumerate(intersection):
		intersec = intersec.split(',')
		intersec.remove('0.0\n')
		intersection[i] = Node(intersec)
	return intersection