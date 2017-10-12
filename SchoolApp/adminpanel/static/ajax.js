$(document).ready(function(){
    get('classeslist', '#classeslist' )// loads list of class
    get('teacherlist', '#teacherlist' ) // loads list of teachers
    //$("#addclassbtn").click(add());
});
var cashe
////////////////////////////////////////////////////////

function showclass(class_id){//shows class members
    get('studentform/initialize/'+class_id,'#editcontainer');
    set_title("Uczniowie w klasie "+class_id)
}
function addclass(){  //adds class
    post($('#new_class').val(), '/add')
    get('classeslist', '#classeslist' )
}
function delclass(teacher_id){ // del class
    post(teacher_id, '/delete')
}

////////////////////////////////////////////////////////

function show_assingedclasses(teacher_name){ // shows classes assinged to teacher
    get('assingedclasses/initialize/'+teacher_name,'#editcontainer')
    set_title("Klasy uczone przez "+teacher_name)
}
function addteacher(){                // adds teacher
    post($('#new_teacher').val(), '/add')
    get('teacherlist', '#teacherlist' )
}
function delteacher(teacher_name){        // deletes teacher
    post(teacher_name, '/delete')
    get('teacherlist', '#teacherlist' )
}

/////////////////////////////////////////////////////////////

function uploadform()
{
     get('studentform/save','#editcontainer'); //add json post
}
function addcell()
{
    element = $('#new_student').val()
    get('studentform/add/'+element,'#editcontainer');//get from form
}
function removecell(student)//maybe in future i will boost it
{
    get('studentform/delete/'+student,'#editcontainer');
}

///////////////////////////////////////////////////////////////

function addclassassigment(){
    get('assingedclasses/add','#editcontainer')
}
function removeclassassigment(){
    get('assingedclasses/delete','#editcontainer')
}
function uploadassigmentform()
{
    get('assingedclasses/save','#editcontainer')
}


///////////////////////////////////////////////////////////////

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
     function set_title(title){
         $("#title").text(title)
     }

