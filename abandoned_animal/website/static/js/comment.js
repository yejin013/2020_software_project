// $("#commentInput").val("test"); // 값셋팅
// var commentModify = document.getElementById('#commentModify');
// // console.log(commentModify.value);

// function modify(){
//     document.getElementById("commentModify").value=input();
// }

var tempcomment;

function commentInput(){
    var inputComment = document.getElementById("commentContent").value;
    tempcomment = inputComment;
}

function output(){
    document.getElementById("output").value = tempcomment;
}