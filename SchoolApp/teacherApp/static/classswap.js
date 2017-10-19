function classswap(id){
$.ajax({
  type: 'GET',
  url: '/teacher/' + id,
}).done(function(response) {
  $('#class_members').html(response);
});
}

function plusPoint(name){
$.ajax({
  type: 'GET',
  url: '/teacher/plus/' + name,
}).done(function(response) {
  $('#class_members').html(response);
});
}

function minusPoint(name){
$.ajax({
  type: 'GET',
  url: '/teacher/minus/' + name,
}).done(function(response) {
  $('#class_members').html(response);
});
}



