"use strict";

$('document').ready(function() {

    // EXAMPLE for how to handle revealTile/flagTile

    // function changeButton(results) {
    //     if (results.confirm === true) {
    //         let theLikeButton = $('#' + String(results.id));
    //         theLikeButton.attr('style', "color:red");
    //     }
    // }

    // Listen for clicks, route appropriately.
    $('.tile').mousedown(function(event) {
        switch (event.which) {
            case 1:
                console.log('left click');
                // Left Mouse button pressed
                // Reveal the tile
                // $.post('/reveal', {'x': this.x, 'y': this.y}, revealTile);
                break;
            case 2:
                console.log('middle click');
                // Middle Mouse button pressed
                // Do nothing
                break;
            case 3:
                console.log('right click');
                // Right Mouse button pressed
                // Flag/Unflag the tile
                // $.post('/flag', {'x': this.x, 'y': this.y}, flagTile);
                break;
            default:
                console.log('default');
                // Do nothing
        }
    });
});
