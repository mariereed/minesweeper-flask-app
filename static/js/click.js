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
        let messageDiv = document.getElementById("row2");
        if (results.confirm === true) {
            revealNewTiles(results.board);
            if (results.gameOver === true) {
                let content = document.createTextNode('You Won!');
                messageDiv.appendChild(content);
                setTimeout(function() {
                    window.location = '/';}, 3000);
            }
        }
        else {
            revealNewTiles(results.board);
            let content = document.createTextNode('Game Over!');
            messageDiv.appendChild(content);
            setTimeout(function() {
                window.location = '/';}, 3000);
        }
    }

    function flagTile(results) {
        if (results.confirm === true) {
            let theTile = document.getElementById("("+ results.x +", " + results.y + ")");
            let classes = theTile.classList;

            let mineCount = document.getElementById('mines');

            if (classes.contains('flagged')) {
                classes.remove('flagged');
                mineCount.innerHTML= eval(mineCount.innerHTML) +1;
            }
            else {
                classes.add('flagged');
                mineCount.innerHTML= eval(mineCount.innerHTML) -1;
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
