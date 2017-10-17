function classswap(id){
$.ajax({
  type: 'GET',
  url: '/teacher/' + id,
}).done(function(response) {
  $('#class_members').html(response);
});
}


