function giveForm(id){
$.ajax({
  type: 'GET',
  url: '/teacher/edit/' + id,
  context: document.body
}).done(function(response) {
  $('#class_members').html(response);
});
}
