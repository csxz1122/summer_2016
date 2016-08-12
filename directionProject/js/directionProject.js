//getting the latlng from the txt file into this variable
var latLng = [];
//a helper for latlng to create an array of arrays 
var helpLatLng =[];
//the google map used
var map;
//the lat and lng that the arrow will follow that google map directions returned
var arrowPath = [];
//the variable for the call to the distance matrix
var intersections = [];
//I possibly need this to keep track of what nodes we are editing instead of using more calls to google api
var counter = 0;
//list of all nodes generated from the intersections
var nodes = [];
//list of the furthest nodes that would be most beneficial to run google directions on
var furIntersections = [];

//***I dont call the distance matrix on all the intersections yet, I also need to deal with the points that are generated 
//from the directions but are not intersections (small curves)

//initializes map, based off the google maps api examples
function initMap() {
	var directionsService = new google.maps.DirectionsService;
	var directionsDisplay = new google.maps.DirectionsRenderer; 
	map = new google.maps.Map(document.getElementById('map'), {
		zoom: 7,
		center: {lat: 34.09668, lng: -117.71978}
	});
	directionsDisplay.setMap(map);

	var onChangeHandler = function() {
          calculateAndDisplayRoute(directionsService, directionsDisplay);
    };

    document.getElementById('start').addEventListener('change', onChangeHandler);
    document.getElementById('end').addEventListener('change', onChangeHandler);
    var school = new google.maps.LatLng(34.10185,-117.71747);

    //take the output of lat lng from the python function that was written to put a 
    //kml into a text file and store this in a two-dimensional array
    jQuery.get('out.txt', function(dataArr) {
        latLng = dataArr.split('\n');
        var j = 0;
        for(i=0; i< latLng.length; i++){
            helpLatLng = latLng[i].split(',');
            latLng[i] =helpLatLng;
            nodes[i] = new Node(latLng[i][1], latLng[i][0], 'yellow', 0, 0);
            intersections[j] = new google.maps.LatLng(latLng[i][1],latLng[i][0]);
            console.log('j1 ' + j);
            if(j==24){
                calculateDistances(intersections,school);
                sleep(1000);
                j=0;
                console.log('j2 ' + j);
            } else {
                j++;
                console.log('j3 ' + j);
                console.log('i ' + i + 'should be ' + latLng.length);
            }

        };
    });

}

function sleep(delay) {
    var start = new Date().getTime();
    while(new Date().getTime() < start + delay);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    var place2 = new google.maps.LatLng(34.10185, -117.71747);
    for(i=0; i<3; i++){
        var place = new google.maps.LatLng(latLng[i][1], latLng[i][0]);        
        directionsService.route({
            origin: place,
            destination: place2,
            travelMode: google.maps.TravelMode.WALKING
        }, function(response, status) {
            if (status === google.maps.DirectionsStatus.OK) {
                // console.log(response.routes[0]);
                arrowPath = response.routes[0].overview_path;
                // directionsDisplay.setDirections(response);
                var lineSymbol = {
                    path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW
                };
                for(x=0; x<arrowPath.length-1; x++){
                    var line = new google.maps.Polyline({
                        path: [{lat:arrowPath[x].lat(), lng: arrowPath[x].lng()}, {lat:arrowPath[x+1].lat(), lng: arrowPath[x+1].lng()}],
                        icons:[{
                            icon: lineSymbol,
                            offset: '100%'
                        }],
                        map: map
                    });
                }

            } else if(status === google.maps.DirectionsStatus.OVER_QUERY_LIMIT){
                i=latLng.length;
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        });
    };
}


// creating a node class to represent intersections 
function Node(lat, lng, color, weight, durr){
    this.lat = lat;
    this.lng = lng;
    this.color = color ;
    this.weight = weight;
    this.durr = durr;
}


function calculateDistances(start, end) {
	// sleep(250);
    var service = new google.maps.DistanceMatrixService();
	service.getDistanceMatrix(
	{
		origins: start,
		destinations: [end],
		travelMode: google.maps.TravelMode.WALKING
	}, callback);
}

function callback(response, status) {
	if (status!= google.maps.DistanceMatrixStatus.OK) {
        console.log('google_error');
		alert('Error was: ' + status);
        // sleep(250);
	} else {
        var distanceVar = response.rows;
		// var origins = response.originAddresses;
		for (var i =0; i < distanceVar.length; i++) {
          if(distanceVar[i].elements[0].duration.value <= 600){
            nodes[counter].color = 'green';
            nodes[counter].durr = distanceVar[i].elements[0].duration.value;
          } else {
            nodes[counter].durr = distanceVar[i].elements[0].duration.value;
            if(nodes[counter].durr > 900){
                furIntersections.push(nodes[counter]);
                nodes[counter].color = 'dark yellow';
            } 
          }//****else compare to the other top 25 and replace the smallest****
          counter++;
          console.log('counter' + counter); 
		}
	}
}