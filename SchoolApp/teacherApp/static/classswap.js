function classswap(id){
$.ajax({
  type: 'POST',
  url: '/teacher/' + id,
}).done(function(response) {
  $('#class_members').html(response);
});
}


