$(document).ready(function(){
    get('classeslist', '#classeslist' )// loads list of class
    get('teacherlist', '#teacherlist' ) // loads list of teachers
    //$("#addclassbtn").click(add());
});

////////////////////////////////////////////////////////

function showclass(class_id){//shows class members
    get('studentform','#editcontainer');
}
function addclass(){  //adds class
    post($('#new_class').val(), '/add')
    get('classeslist', '#classeslist' )
}
function delclass(class_id){ // del class
    post(class_id, '/delete')
}

////////////////////////////////////////////////////////

function show_assingedclasses(){ // shows classes assinged to teacher

}
function addteacher(){                // adds teacher
    post($('#new_teacher').val(), '/add')
    get('teacherlist', '#teacherlist' )
}
function delteacher(teacher_name){        // deletes teacher
    post(teacher_name, '/delete')
    get('teacherlist', '#teacherlist' )
}

    function get(item, place){
            $.ajax({
                 type: 'GET',
                 url: '/admin/' + item,
            }).done(function(response){
                $(place).html(response);
            });
     }
     function post(data,command){
            $.ajax({
                url: "/admin/classeslist" + command,
                type: "POST",
                data: JSON.stringify(data),
                contentType: "application/json",
        });
     }

