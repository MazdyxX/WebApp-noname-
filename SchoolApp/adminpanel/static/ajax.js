$(document).ready(function(){
    get('classeslist', '#classeslist' )// loads list of class
    get('teacherlist', '#teacherlist' ) // loads list of teachers
    //$("#addclassbtn").click(add());
});
function showclass(){
get('studentform','#editcontainer');
}
function addclass(){
post(
$('#txt_name').val()
;)
get('classeslist', '#classeslist' )
}
function delclass(){

}


    function get(item, place){
            $.ajax({
                 type: 'GET',
                 url: '/admin/' + item,
            }).done(function(response){
                $(place).html(response);
            });
     }
     function post(data){
            $.ajax({
                url: "/admin/classeslist",
                type: "POST",
                data: JSON.stringify(data),
                contentType: "application/json",
        });
     }

