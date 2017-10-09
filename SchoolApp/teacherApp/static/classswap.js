function classswap(id){
$.ajax({
  type: 'GET',
  url: "/teacher/" + id,
  context: document.body
}).done(function(response) {
  $('class_members').html(response);
});
}