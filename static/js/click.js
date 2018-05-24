"use strict";

$('document').ready(function() {

    // EXAMPLE for how to handle revealTile/flagTile

    // function changeButton(results) {
    //     if (results.confirm === true) {
    //         let theLikeButton = $('#' + String(results.id));
    //         theLikeButton.attr('style', "color:red");
    //     }
    // }
    function revealTile(results) {
        if (results.confirm === true) {
            console.log('Success Reveal');
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
