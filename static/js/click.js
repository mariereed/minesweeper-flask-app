"use strict";

$('document').ready(function() {
    function revealTile(results) {
        let height = results.board.length;
        let width  = results.board[0].length;
        if (results.confirm === true) {
            for (let i = 0; i < width; i++) {
                for (let j = 0; j < height; j++) {
                    if (results.board[i][j] !== "?") {
                        let theTile = document.getElementById("("+ i +", " + j + ")");
                        if (theTile.hasChildNodes()) { continue; }
                        let content = document.createTextNode(results.board[i][j]);
                        theTile.appendChild(content);
                        theTile.className += " revealed";
                    }
                }
            }
            if (results.gameOver === true) {
                alert('You Won!');
                window.location = '/';
            }
        }
        else {
            for (let i = 0; i < width; i++) {
                for (let j = 0; j < height; j++) {
                    if (results.board[i][j] !== "?") {
                        let theTile = document.getElementById("("+ i +", " + j + ")");
                        if (theTile.hasChildNodes()) { continue; }
                        let content = document.createTextNode(results.board[i][j]);
                        theTile.appendChild(content);
                        theTile.className += " revealed";
                    }
                }
            }
            alert('You hit a mine! Game Over.');
            // window.location = '/';
        }
    }

    function flagTile(results) {
        if (results.confirm === true) {
            console.log('In Flag Tile Function');
        }
    }
    // Listen for clicks, route appropriately.
    $('.tile').mousedown(function(event) {
        switch (event.which) {
            case 1:
                $.post('/reveal', {'coordinates': this.id}, revealTile);
                break;
            case 2:
                break;
            case 3:
                $.post('/flag', {'coordinates': this.id}, flagTile);
                break;
            default:
                break;
        }
    });
});
