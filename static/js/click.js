"use strict";

$('document').ready(function() {
    function revealNewTiles(board) {
        let height = board.length;
        let width  = board[0].length;
        for (let i = 0; i < width; i++) {
            for (let j = 0; j < height; j++) {
                if (board[i][j] !== "?") {
                    let theTile = document.getElementById("("+ i +", " + j + ")");
                    if (theTile.hasChildNodes()) { continue; }
                    let content = document.createTextNode(board[i][j]);
                    theTile.appendChild(content);
                    theTile.className += " revealed";
                }
            }
        }
    }
    function revealTile(results) {
        if (results.confirm === true) {
            revealNewTiles(results.board);
            if (results.gameOver === true) {
                alert('You Won!');
                window.location = '/';
            }
        }
        else {
            revealNewTiles(results.board);
            alert('You hit a mine! Game Over.');
            // window.location = '/';
        }
    }

    function flagTile(results) {
        if (results.confirm === true) {
            let theTile = document.getElementById("("+ results.x +", " + results.y + ")");
            let classes = theTile.classList;
            if (classes.contains('flagged')) {
                classes.remove('flagged');
            }
            else {
                classes.add('flagged');
            }
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
