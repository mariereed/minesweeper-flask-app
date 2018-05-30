"use strict";

$('document').ready(function() {
    
    var seconds = 0, minutes = 0, hours = 0, t;
    let timerDiv = document.getElementById('timer');

    function add() {
        seconds++;
        if (seconds >= 60) {
            seconds = 0;
            minutes++;
            if (minutes >= 60) {
                minutes = 0;
                hours++;
            }
        }
    
        timerDiv.textContent = (hours ? (hours > 9 ? hours : "0" + hours) : "00") + ":" + (minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" + (seconds > 9 ? seconds : "0" + seconds);

        timer();
    }

    function timer() {
        t = setTimeout(add, 1000);
    }


    let board = document.getElementById('board');

    board.addEventListener("click", function(event) {
        if (board.classList.contains('started')) {
            return;
        }
        board.classList.add('started');
        console.log('timer started');
        timer();
        // var start = new time
        // var elapsed = timeNow - start
        // display time every one second.
    });

});
