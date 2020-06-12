// function modifyData(){
//     confirm("수정하시겠습니까?");
// }

function deleteCheck(){
  alert("게시글 권한이 없습니다.")
}

function deleteConfirm(n) {
  if (confirm("이 포스트를 삭제하시겠습니까?")) {
      window.location.href = "/website/delete/" + n;
  } else {
      return false;
  }
}

function commentDeleteConfirm(n) {
  if (confirm("이 댓글을 삭제하시겠습니까?")) {
      window.location.href = "/website/comment/delete/" + n;
  } else {
      return false;
  }
}

function cancleForm(){
<<<<<<< HEAD
  if(confirm("이 페이지를 벗어나면 마지막 저장 후 수정된 내용은 저장되지 않습니다.")){
    window.location.href = "/website/mypage/";
  }
  else {
      return false;
  }
=======
    if(confirm("이 페이지를 벗어나면 마지막 저장 후 수정된 내용은 저장되지 않습니다.")){
      window.location.href = "/website/mypage/";
    }
    else {
        return false;
    }
  
>>>>>>> f7774f3f88780dffa97611f6977b9a17521e265e
}

function secedeForm(n){
  if(confirm("정말로 탈퇴하시겠습니까?")){
<<<<<<< HEAD
    window.location.href = "/website/mypage/myinfo/delete/" + n;
=======
      window.location.href = "/website/mypage/myinfo/delete/" + n;
>>>>>>> f7774f3f88780dffa97611f6977b9a17521e265e
  } else {
      return false;
  }
}

$(function() {
  $("#modify").on("click", function() {
    $("divToggle").toggle();
  });
});