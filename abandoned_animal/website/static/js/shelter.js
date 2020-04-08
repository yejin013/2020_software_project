// 전역변수 생성
var mylat = 0; // 사용자의 위도
var mylng = 0; // 사용자의 경도
var shelterlat = 0; // 보호소의 위도
var shelterlng = 0; // 보호소의 경도
var short = 0;
var showlat; // 보여줄 위도
var showlng; // 보여줄 경도


// 사용자 위도, 경도 받기
function getMyLocation() {
    if (navigator.geolocation) { // GPS를 지원하면
      navigator.geolocation.getCurrentPosition(function(position) {
        mylat = position.coords.latitude;
        mylng = position.coords.longitude;
      }, function(error) {
        console.error(error);
      }, {
        enableHighAccuracy: false,
        maximumAge: 0,
        timeout: Infinity
      });
    } else {
      alert('GPS를 지원하지 않습니다');
    }
}


// 보호소 위도, 경도 받기
function shelterInfo(lat, lng){
  shelterlat = lat;
  shelterlng = lng;

  getMyLocation();
  distHaversine(shelterlat, shelterlng)
  init();
}


// 거리 비교
rad = function(x) {return x*Math.PI/180;}

function distHaversine(shelterlat, shelterlng){
	var R = 3960; // earth's mean radius in mi
	var dLat  = rad(shelterlat - mylat);
	var dLong = rad(shelterlng - mylng);

	var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
	        Math.cos(rad(mylat)) * Math.cos(rad(shelterlat)) * Math.sin(dLong/2) * Math.sin(dLong/2);
	var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
	var d = R * c;

  short = d.toFixed(1);
  compareDistance(d.toFixed(1));
}

function compareDistance(distance){
  if (short >= distance){
    short = distance;
    showlat = shelterlat;
    showlng = shelterlng;  
  }
}

// 사용자 위치 출력
function userinit()
{
  window.navigator.geolocation.getCurrentPosition(current_position);
}
 
function current_position(position)
{
  var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  var map_options = {
        center:latlng,zoom:14,
        mapTypeId:google.maps.MapTypeId.ROADMAP,
        mapTypeControl:false,
        navigationControlOptions:{style:google.maps.NavigationControlStyle.SMALL}
    }
    
    var map = new google.maps.Map(document.getElementById("google_map"), map_options);
    
    var marker = new google.maps.Marker({position:latlng,map:map,title:"You are here!"});
}


// 사용자 위치 출력 함수 호출
window.addEventListener("load", userinit);



// 보호소 위치 출력
function init()
{
  window.navigator.geolocation.getCurrentPosition(shelter_position_init);
}
 
function shelter_position_init(position)
{
  var latlng = new google.maps.LatLng(showlat, showlng);
  var map_options = {
        center:latlng,zoom:14,
        mapTypeId:google.maps.MapTypeId.ROADMAP,
        mapTypeControl:false,
        navigationControlOptions:{style:google.maps.NavigationControlStyle.SMALL}
    }
    
    var map = new google.maps.Map(document.getElementById("google_map"), map_options);
    
    var marker = new google.maps.Marker({position:latlng,map:map,title:"You are here!"});
}



// 보호소 정보 띄우기
$(document).ready(function () {
  $(".shelter-form").css("display", "none");
  $("#hide").click(function () {
      $(".shelter-form").css("display", "none");
    })
  $("#show").click(function () {
      $(".shelter-form").css("display", "");
  })
});