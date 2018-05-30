"use strict";

$('document').ready(function() {
    
    var seconds = 0, minutes = 0, hours = 0, t;
    let timerDiv = document.getElementById('timer');




    let board = document.getElementById('board');

    board.addEventListener("click", function(event) {
        if (board.classList.contains('started')) {
            return;
        }
        board.classList.add('started');
        console.log('timer started');
        // var start = new time
        // var elapsed = timeNow - start
        // display time every one second.
    });

});
