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


// 사용자 위치 출력
function userinit()
{
  window.navigator.geolocation.getCurrentPosition(current_position);
}
 
function current_position(position)
{
  var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  document.getElementById("userlat").innerHTML=position.coords.latitude;
  document.getElementById("userlng").innerHTML=position.coords.longitude;
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
function init(lat, lng)
{
  showlat = lat;
  showlng = lng;
  window.navigator.geolocation.getCurrentPosition(shelter_position_init);
}
 
function shelter_position_init(position)
{
  var latlng = new google.maps.LatLng(showlat, showlng);
  document.getElementById("showlat").innerHTML=showlat;
  document.getElementById("showlng").innerHTML=showlng;
  var map_options = {
        center:latlng,zoom:14,
        mapTypeId:google.maps.MapTypeId.ROADMAP,
        mapTypeControl:false,
        navigationControlOptions:{style:google.maps.NavigationControlStyle.SMALL}
    }
    
    var map = new google.maps.Map(document.getElementById("google_map"), map_options);
    
    var marker = new google.maps.Marker({position:latlng,map:map,title:"You are here!"});

    return [showlat, showlng];
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