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
        $("#dodajuczniarow").before("<div  class='row rowborder'> ");
    });

    $("#dodajucznia").click(function(){
        $("#dodajuczniarow").before("<div  class='row rowborder'></div> ");
    });


});
</script>



