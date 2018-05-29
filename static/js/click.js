"use strict";

$('document').ready(function() {
    function revealTile(results) {
        if (results.confirm === true) {
            console.log('Success Reveal');

            let height = results.board.length;
            let width  = results.board[0].length;

            for (let i = 0; i < width; i++) {
                for (let j = 0; j < height; j++) {
                    if (results.board[i][j] !== "?") {
                        // fill in value for that tile
                        let theTile = document.getElementById("("+ i +", " + j + ")");
                        if (theTile.hasChildNodes()) {
                            break;
                        }
                        let content = document.createTextNode(results.board[i][j]);
                        theTile.appendChild(content);
                        theTile.className += " revealed";
                    }
                }
            }
        }
        else {
            // reveal mines with current board
            // game over
        }
    }

    function flagTile(results) {
        if (results.confirm === true) {
            console.log('Success Flag');
        }
    }
    // Listen for clicks, route appropriately.
    $('.tile').mousedown(function(event) {
        switch (event.which) {
            case 1:
                console.log('left click');
                console.log(this.id);
                // Left Mouse button pressed
                // Reveal the tile
                $.post('/reveal', {'coordinates': this.id}, revealTile);
                break;
            case 2:
                console.log('middle click');
                // Middle Mouse button pressed
                // Do nothing
                break;
            case 3:
                console.log('right click');
                console.log(this.id);
                // Right Mouse button pressed
                // Flag/Unflag the tile
                $.post('/flag', {'coordinates': this.id}, flagTile);
                break;
            default:
                console.log('default');
                // Do nothing
        }
    });
});
