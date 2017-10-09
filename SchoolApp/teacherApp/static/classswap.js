function classswap(id){
$.ajax({
  type: 'POST',
  url: '/teacher/' + id,
}).done(function(response) {
  $('#class_members').html(response);
});
}

function giveForm(id){
$.ajax({
  type: 'GET',
  url: '/teacher/edit/' + id,
  context: document.body
}).done(function(response) {
  $('#class_members').html(response);
});
}