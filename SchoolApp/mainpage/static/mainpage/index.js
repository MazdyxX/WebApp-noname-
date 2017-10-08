function login(){
$.ajax({
  type: 'GET',
  url: "/login",
  context: document
}).done(function(response) {
  $('html').html(response);
});
}