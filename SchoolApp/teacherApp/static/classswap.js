function classswap(id){
$.ajax({
  type: 'GET',
  url: "/" + id,
  context: document
}).done(function(response) {
  $('class_members').html(response);
});
}