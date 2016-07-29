# Must take out the the link in the KML (of the file before this will work). **POSSIBLY FIX THIS***
# This function will take in a KML file that has points at each of the intersections and create a file 
# that has the lat and lng separated by commas and each of these separated by a new line


import xml.etree.ElementTree as ET

def kmlParse(kml):
	tree = ET.parse(kml)
	root = tree.getroot()
	file = open('/Users/cssummer16/Desktop/summer_2016/python/out.txt', 'w')
	for x in root.findall(".//Placemark"):
		file.write(x.find("Point/coordinates").text + '\n')
	file.close()
	return 'out.txt'
