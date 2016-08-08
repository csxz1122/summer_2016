# summer_2016

##File Descriptions
###pointFunction.py
  
**Functions**

  * __kmlParse__
    * __What it does:__ Takes in a kml file and text_file location as an argument and returns a text file that has lng and lat separeted by commas and each point is distinguised by a new line
   * __Future:__ Fix that this function does not work if the file is directly imported from google maps and has the line <kml xmlns='http://www.opengis.net/kml/2.2'> but if the link is removed but the tag is left (<kml>) the function runs just fine. 

###intersectionParse.py

  **Class**

  __Node Class__

  * Each intersection is stored as a node, that holds the color, distance, lat, lng and value (or how many times this node is used on the paths to school). It defines the equal, less than, hash and subtraction for nodes.
  * __Future:__ Nothing is done with the color stored, and not all colors are being updated, there is currently a default value since there are not multiple calls for directions (this has not been implemented yet)
  
**Functions**
     
* __createIntersections__
* __What it does:__ Splits the input text file generated from the kmlParse function by comma and removes an extra '0.0' and the \n and returns this as an array. 

###addRouteToMap.py
  **Functions**

  * __addRoute__
    * __What it does:__  Takes in a dictionary (mapOfNodes), a list of intersections, a list created from intersections but intersections are removed from this list to prevent repeat direction calls and an array of points returned from google maps directions. For the points in the input list it checks if it is in directionIntersections and removes it if it is. It then finds the distance between the lat and lng and if it is more than a set threshold then close intersections that might be on the path are found and then compared to a threshold if they are lower than the threshold they are sorted and added to the path. 
    * __Future:__ There is a place that currently has a print statements that says 'not done yet' this portion will need to be written to incorporate multiple direction calls. If they already exist in the mapOfNodes go through and update the value (in the future maybe update colors).
  * __snapToIntersection__
    * __What it does:__  Itmakes a call to interExist for each point in the list of points
  * __interExist__
    * __What it does:__  It is a helper function to snapToIntersection and it checks to see if the point matches an intersection with in the threshold, if it does it returns the intersection if not it returns the point.
  * __getSpPount__
    * __What it does:__ Finds the projection of a point onto a line and if that projection is below the threshold it is added to the list of missing_intersections.
* **Future**  


###dirProject.py
__Functions__

* __main__
  * __What it does:__  Gets directions from google maps and stores the points and distance returned from google maps and send this information to addRoute, a function located in addRouteToMap.py. Then for every key in mapOfNodes it adds a path, then the point for the school and draws the map which generates an html file using pygmaps.
  * __How it works:__ Google maps directions api returns the results as a dictionary, gmaps is a variable that makes a call to googlemaps (an imported library) with the API key that is required and free to get from google. Points stores the latitude and longitude of places the polyline follows, distance stores how long traveling takes in seconds.
  * __Future:__ 


**Variables and other things**

* The kml_file was generated using 'my google maps' I placed a marker at each intersection and exported it as a .kml file. 

* _Future:_ Change the school point on the map to a custom logo possibly the schools mascot. 

###pygmaps.py
* I got this from a retired python module found [here] (https://code.google.com/archive/p/pygmaps/)
* __Modifications__ I added variables to the map class to include weight and count, the weight of each node is stored in an array and then when the path is count is incremented so that the corresponding weight goes to the node. I also modified draw polyline to edit the html generated and to include the arrows along with changing the thickness of the arrow. 
* __Future:__ How to determine the weight from the value, if the value is 8 then the line will become very thick if the strokeWeight is set to 8. Right now it is being divided by 2 in drawpaths. 