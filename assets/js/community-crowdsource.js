function getPosition() {
	GeoMarker.setMap(map);
	$("#geoButton").attr('onclick', 'turnPositionOff()')
}

function turnPositionOff() {
	GeoMarker.setMap(null)
	$("#geoButton").attr('onclick', 'getPosition()')
}

setTimeout(function() {
	$("img[src*='googleapis']").each(function() {
		$(this).attr("src", $(this).attr("src") + "&" + (new Date()).getTime());
	});
}, 3000);

function addLocation() {
	$('#message').html('<div class="alert alert-info"><a class="close" data-dismiss="alert" href="#">&times;</a>Click on the location you would like to report, then click the marker to report it</div>')
	google.maps.event.addListener(map, 'click', function(e) {
		tempMarker.setMap(null)
		tempMarker = new google.maps.Marker({
			draggable : true,
			animation : 'DROP',
			position : e.latLng,
			clickable : true,
			map : map
		})
		google.maps.event.addListener(tempMarker, 'click', function(e) {
			removeAddStuff();
		})
	})
}

function removeAddStuff() {
	latLng = new google.maps.LatLng((tempMarker.position.Ya), (tempMarker.position.Za));
	latlng = [tempMarker.position.Ya, tempMarker.position.Za]
	var formattedAddress = "";
	geocoder.geocode({
		'latLng' : latLng
	}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			if (results[0]) {
				formattedAddress = results[0].formatted_address;
				$('[name=Address]').val(formattedAddress);
			} else {
				alert('No results found');
			}
		} else {
			alert('Geocoder failed due to: ' + status);
		}
	});
	$('#dataModal').modal({
	})
	$('#dataModal').on('shown', function() {
		var d = new Date();
		$('[name="Date Recorded"]').val(new Date().toJSON().substring(0, 10))
		$('[name="Number of Tires"]').val(1);
		$('[name=latLng]').val(latlng);
	})
	setTimeout();
}

function handleNoGeolocation(errorFlag) {
	if (errorFlag == true) {
		alert("Geolocation service failed.");
	} else {
		alert("Oops, your browser does not support geolocation, please try another browser");
	}
}