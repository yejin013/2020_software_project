// document.getElementsByName("testText")[0].onkeydown = function(e){
//     var eventCode = e.code;
// };

// document.getElementsByName("testText")[0].onkeyup = function(e){
//     if(e.code == 'Backspace'){
//         document.getElementById("test").innerHTML = "";
//     }
// };

function onlyNumber(event){
    event = event || window.event;
    var keyID = (event.which) ? event.which : event.keyCode;
    if ( (keyID >= 48 && keyID <= 57) || (keyID >= 96 && keyID <= 105) || keyID == 8 || keyID == 46 || keyID == 37 || keyID == 39 ) 
        return;
    else
        return false;
}
 
function removeChar(event) {
    event = event || window.event;
    var keyID = (event.which) ? event.which : event.keyCode;
    if ( keyID == 8 || keyID == 46 || keyID == 37 || keyID == 39 ) 
        return;
    else
        event.target.value = event.target.value.replace(/[^0-9]/g, "");
}

function fn_pw_check() {
    var pw = document.getElementById("pw").value; //비밀번호
    var pw2 = document.getElementById("pwChk").value; // 확인 비밀번호

    var pattern1 = /[0-9]/;
    var pattern2 = /[a-zA-Z]/;
    var pattern3 = /[~!@\#$%<>^&*]/;     // 원하는 특수문자 추가 제거

    if(pw != pw2) {
        alert("비밀번호가 일치하지 않습니다.");
        return false;
    }

//    if(!pattern1.test(pw)||!pattern2.test(pw)||!pattern3.test(pw)||pw.length<8||pw.length>50){
//         alert("영문+숫자+특수기호 8자리 이상으로 구성하여야 합니다.");
//         return false;
//     }          

    return true;
}