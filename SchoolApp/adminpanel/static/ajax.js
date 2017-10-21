$(document).ready(function(){
    get('classeslist', '#classeslist' )// loads list of class
    get('teacherlist', '#teacherlist' ) // loads list of teachers
});
    //$("#addclassbtn").click(add());
////////////////////////////////////////////////////////

function showclass(class_id){//shows class members
    get('studentform/initialize/'+class_id,'#editcontainer');
    set_title("Klasa "+class_id)
}
function addclass(){  //adds class
    post($('#new_class').val(), '/add')
    get('classeslist', '#classeslist' )
}
function delclass(teacher_id){ // del class
    post(teacher_id, '/delete')
}
       function loadformdata(){
            var data = [];
                 dt = $('').val()
              data.push(dt);
         console.log(data[0]);
        return data
}
function test(){
console.log("test")
}

////////////////////////////////////////////////////////

function show_assingedclasses(teacher_name){ // shows classes assinged to teacher
    get('assingedclasses/'+teacher_name,'#editcontainer')
    set_title(teacher_name)
}
function addteacher(){                // adds teacher
    get('teacherlist/add/'+$('#new_teacher').val(),'#teacherlist')
    get('teacherlist', '#teacherlist' )
}
function delteacher(teacher_name){        // deletes teacher
    get('teacherlist/delete/'+teacher_name, '#teacherlist' )
    get('teacherlist', '#teacherlist' )
}

/////////////////////////////////////////////////////////////

function uploadform()
{
     get('studentform/save', '#editcontainer'); //add json post
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
    dt = $("#new_assign").val();
    console.log(dt)
    get('changeassigment/add/'+dt,'#editcontainer')
}
function removeclassassigment(element){
    get('changeassigment/delete/'+element,'#editcontainer')
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
 function postlist(data,command){
        $.ajax({
            url: "/admin/" + command,
            type: "POST",
            data: JSON.stringify(data),
            contentType: "application/json",
    });
 }
 function set_title(title){
     $("#title").text(title)
 }
 ////////////////////////////////////////////////////////////////
function studentcodes(){
    get('generate/students','#editcontainer');

}

function teachercodes(){
    get('generate/teacher','#editcontainer');
}

