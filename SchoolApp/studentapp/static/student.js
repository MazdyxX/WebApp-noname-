function play(){
window.location.href='/student/game';
}

function achivements(){
window.location.href='/student/achivements';
}

function ranktable(){
window.location.href='/student/ranking';
}

function getranking(){
        console.log("getting")
        $.ajax({
             type: 'GET',
             url: '/student/ranking/trophies',
        }).done(function(response){
            $('#ranks').html(response);
        });
 }

 ////////////////---GAME--- ////////////////
 function upgrade(object){
    window.location.href='/student/game/upgrade/'+ object;
 }
