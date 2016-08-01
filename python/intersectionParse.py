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
		intersection[i].latlng[0] = round(float(intersection[i].latlng[0]),5)
		intersection[i].latlng[1] = round(float(intersection[i].latlng[1]),5)
	return intersection