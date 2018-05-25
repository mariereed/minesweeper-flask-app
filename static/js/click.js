"use strict";

$('document').ready(function() {
    function revealTile(results) {
        if (results.confirm === true) {
            console.log('Success Reveal');
            // For each tile in results.board that does not have a '?' value...
            // change the tile to its corresponding value (5,4,3,2,1,blank)
            let fill = "(0, 0)";
            let theDiv = document.getElementById(fill);
            let content = document.createTextNode("?");
            theDiv.appendChild(content);
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
