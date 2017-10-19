function loginteacher(){
$.ajax({
  type: 'GET',
  url: "/teacher/login",
  context: document
}).done(function(response) {
  $('html').html(response);
});
}function loginstudent(){
$.ajax({
  type: 'GET',
  url: "/student/login",
  context: document
}).done(function(response) {
  $('html').html(response);
});
}

