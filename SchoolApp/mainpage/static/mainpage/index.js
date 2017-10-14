function loginteacher(){
$.ajax({
  type: 'GET',
  url: "/loginteacher",
  context: document
}).done(function(response) {
  $('html').html(response);
});
}function loginstudent(){
$.ajax({
  type: 'GET',
  url: "/loginstudent",
  context: document
}).done(function(response) {
  $('html').html(response);
});
}