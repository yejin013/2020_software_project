var mylat;
var mylng;

function gpsCheck(){
  if (confirm("GPS 기능을 사용하시겠습니까? (미사용시, 서비스 이용이 불가능할 수도 있습니다.)")) {      
    if (navigator.geolocation) { // GPS를 지원하면
      navigator.geolocation.getCurrentPosition(function(position) {
        mylat = position.coords.latitude;
        mylng = position.coords.longitude;
        window.location.href = "/website/shelter?" + "lat=" + mylat + "&lng=" + mylng;
        alert(mylat)
  
      }, function(error) {
        console.error(error);
      }, {
        enableHighAccuracy: false,
        maximumAge: 0,
        timeout: Infinity
      });
    } else {
      alert('GPS를 지원하지 않습니다');
      window.location.href = "/website/shelter/";
    }
} else {
  window.location.href = "/website/shelter/";
}
}