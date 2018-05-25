
from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import os
import minesweeper


# -------- Set Up ----------------------------------------------

app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
# Raise error for undefined variable
app.jinja_env.undefined = StrictUndefined

# -------- Routes ----------------------------------------------


@app.route('/')
def homepage():
    """ Application page."""

    height    = 8
    width     = 8
    mineCount = 10

    flagCount = 0

    true_false_matrix      = minesweeper.createBeginnerTrueFalseMatrix(height, width, mineCount)
    number_and_mine_matrix = minesweeper.numberFill(true_false_matrix)
    blank_matrix           = minesweeper.createNewBlankMatrix(true_false_matrix)

    print minesweeper.tabulateMatrix(number_and_mine_matrix)

    session['number_and_mine_board'] = number_and_mine_matrix
    session['current_board'] = blank_matrix

    return render_template('base.html', tile_grid=true_false_matrix)


@app.route('/reveal', methods=["POST"])
def revealTile():
    """ Reveal the selected tile. """

    full_board    = session.get('number_and_mine_board')
    current_board = session.get('current_board')

    x, y = eval(request.form.get('coordinates'))
    was_revealed, board = minesweeper.revealClick(x, y, full_board, current_board)

    print minesweeper.tabulateMatrix(board)
    session['current_board'] = board

    if was_revealed:
        print 'Revealed a tile'
        return jsonify({'confirm': True, 'board': board})
    else:
        print 'Hit a mine'
        return jsonify({'confirm': False, 'board': board})


@app.route('/flag', methods=["POST"])
def flagTile():
    """ Reveal the selected tile. """
    # Place flag, unless already flagged then unflag
    print 'made it into flag'
    return jsonify({'confirm': True})


if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    app.debug = True
    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
