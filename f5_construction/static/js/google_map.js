function initMap() {
  var f5_construction = {lat: 30.3080538, lng: -98.0342811};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: f5_construction
  });
  var marker = new google.maps.Marker({
    position: f5_construction,
    map: map
  });
}
