"use strict";

var t;

$('document').ready(function() {
    
    var seconds = 0, minutes = 0, hours = 0;
    let timerDiv = document.getElementById('timer');
    let board = document.getElementById('board');

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

    board.addEventListener("click", function(event) {
        if (board.classList.contains('started')) {
            return;
        }
        board.classList.add('started');
        timer();
    });

});
