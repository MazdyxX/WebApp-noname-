# WebApp-noname-
Created by Maksymilian Demitraszek


Html nameofapp/templates /-/-/
css and js nameofapp/static

<script>
$(document).ready(function(){
    $("#dodajoddzialbtn").click(function(){
        $("#dodajodrow").before("");
    });

    $("#dodajoddzialbtn").click(function(){
        $("#dodajodrow").before("<div  class='row rowborder'></div> ");
    });

    $("#dodajucznia").click(function(){
        $("#dodajuczniarow").before("<div  class='row rowborder'> <form class='col s12'><div class='row'><div class='input-field col s6'><input placeholder='Nazwisko i imię' id='first_name' type='text' class='validate'><label for='first_name'>First Name</label></div></div> <button class='btn waves-effect waves-light' type='submit' name='action'>Submit<i class='material-icons right'>send</i></button></form></div>");
    });

    $("#dodajucznia").click(function(){
        $("#dodajuczniarow").before("<div  class='row rowborder'></div> ");
    });


});
</script>



