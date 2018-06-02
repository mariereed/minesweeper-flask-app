"use strict";

$('document').ready(function() {
    function reloadIt(returned_stuff) {
        document.location.reload();
    }
    let beginner = document.getElementById('beginner');
    beginner.addEventListener("click", function(event) {
        $.post('/mode', {'mode': 'beginner'}, reloadIt);
    });

    let intermediate = document.getElementById('intermediate');
    intermediate.addEventListener("click", function(event) {
        $.post('/mode', {'mode': 'intermediate'}, reloadIt);
    });

    let advanced = document.getElementById('advanced');
    advanced.addEventListener("click", function(event) {
        $.post('/mode', {'mode': 'advanced'}, reloadIt);
    });

});
