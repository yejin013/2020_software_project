// function modifyData(){
//     confirm("수정하시겠습니까?");
// }

<<<<<<< HEAD
// function removeData(){
//     confirm("정말로 삭제하시겠습니까?");
// }

=======
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
>>>>>>> ab25f280aa52591a9761bb4cc11081b07b161871

function cancleForm(){
    confirm("이 페이지를 벗어나면 마지막 저장 후 수정된 내용은 저장되지 않습니다.");
}

function secedeForm(){
  confirm("정말로 탈퇴하시겠습니까?")
}

$(function() {
    $("#modify").on("click", function() {
      $("divToggle").toggle();
    });
<<<<<<< HEAD
  });
=======
  });

  
>>>>>>> ab25f280aa52591a9761bb4cc11081b07b161871
