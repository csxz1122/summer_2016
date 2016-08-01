# summer_2016

##File Descriptions
###pointFunction.py
  
**Functions**

  * __kmlParse__
    * __What it does:__ Takes in a kml file as an argument and creates a text file that has lng and lat separeted by commas and each point is distinguised by a new line
   * __Future:__ Fix that this function does not work if the file is directly imported from google maps and has the line <kml xmlns='http://www.opengis.net/kml/2.2'> but if the link is removed but the tag is left (<kml>) the function runs just fine. 

###intersectionParse.py

  **Class**

  __Node Class__

  * Each intersection is stored as a node, this holds the color, distance, latlng and value (or how many times this node is used on the paths to school)
  * __Future:__ Nothing is done with the color stored, and not all colors are being updated, there is currently a default value since there are not multiple calls for directions (this has not been implemented yet)
  
**Functions**
     
* __createIntersections__
* __What it does:__ Splits the input text file generated from the kmlParse function by comma and removes an extra '0.0' and the \n and returns this as an array. Rounds and turns the strings into a float, this is to try to get the arrows to begin where the previous arrow ended. This solution has made the problem better but not completely solved it.

###addRouteToMap.py
  **Functions**

  * __addRoute__
    * __What it does:__  Takes in a dictionary (mapOfNodes), an array of intersections, and an array of points returned from google maps directions. For the points in the directions it checks if the points match an intersection, if it doesn't match it checks if it is in the dictionary already (the rest of this isnt finished) if it is not already in the dictionary then it adds an entry using the node as a key and the previous node as a value. If it matches an entry in the dictionary then it is removed from the array of intersections and then repeats the same as above and returns the mapOfNodes
    * __Future:__ There is a place that currently has a print statements that says 'not done yet' this portion will need to be written to incorporate multiple direction calls. If they already exist in the mapOfNodes go through and update the value (in the future maybe update colors). 
  * __interExist__
    * __What it does:__  It is a helper function to addRoute and it checks to see if the point matches an intersection with .0001101 accuracy, if it does it edits the intersection by converting the latlng to a float and rounding it in attempt to fix the crooked arrows that were being generated. If there was an intersection match it returns the intersection if not it returns false   
* **Future**  


###dirProject.py
__Functions__

* __callDirections__
  * __What it does:__  Gets directions from google maps and stores the points and distance returned from google maps and send this information to addRoute, a function located in addRouteToMap.py. 
  * __How it works:__ Google maps directions api returns the results as a dictionary, gmaps is a variable that makes a call to googlemaps (an imported library) with the API key that is required and free to get from google. Points stores the latitude and longitude of places the polyline follows, distance stores how long traveling takes in seconds.
  * __Future:__ This function will need to make multiple calls to get the directions from each item in intersection, right now it is easier to just use one since google maps has limits on the amount of calls you can make per second and total in a day. The distance variable is not being used but might be helpful in the future when combining the isochrone map and the flow of direction (arrow map)
* __updateMap__
  * __What it does:__  Makes a call to callDirections, and initializes a map using pygmaps, then for each item in the dictionary, MapOfNodes, it creates a path by calling addpath (located in pygmaps.py)
  * _How it works:_ This is creating an HTML file that will create all the items, it has not generated the file but this needs to be called before the draw function in pygmaps is called to initilize the map (the draw function creates the HTML file). 

**Variables and other things**

* The kml_file was generated using 'my google maps' I placed a marker at each intersection and exported it as a .kml file. 
* The Map variables are the settings of the google maps and the HTML_NAME is what the html file generated will be called
* _Future:_ Put the calls to kmlParse, and createIntersection into a main function along with updateMAp and THE_MAP.draw(), change the school point on the map to a custom logo possibly the schools mascot. 

###pygmaps.py
* I got this from a retired python module found [here] (https://code.google.com/archive/p/pygmaps/)
* __Modifications__ I added variables to the map class to include weight and count, the weight of each node is stored in an array and then when the path is count is incremented so that the corresponding weight goes to the node. I also modified draw polyline to edit the html generated and to include the arrows along with changing the thickness of the arrow. 
* __Future:__ How to determine the weight from the value, if the value is 8 then the line will become very thick if the strokeWeight is set to 8. Right now it is being divided by 2 in drawpaths. 