function classswap(id){
$.ajax({
  type: 'GET',
  url: '/teacher/' + id,
  context: document
}).done(function(response) {
  $('html').html(response);
});
}