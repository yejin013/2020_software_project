// function modifyData(){
//     confirm("수정하시겠습니까?");
// }

function deleteCheck(){
  alert("게시글 권한이 없습니다.")
}

function removeData(){
    confirm("정말로 삭제하시겠습니까?");
    if(confirm("정말로 삭제하시겠습니까?")==true){
      location.href ='{% url "website:delete" post_id=post.id %}'
    }
}

function commentRemoveData(){
    confirm("정말로 삭제하시겠습니까?");
    if(confirm("정말로 삭제하시겠습니까?")==true){
      location.href ='{% url "website:comment_delete" comment_id=comment.id %}'
    }
}

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
  });