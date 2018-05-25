
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

    preMatrix     = minesweeper.createBeginnerTrueFalseMatrix(height, width, mineCount)
    numberMatrix  = minesweeper.numberFill(preMatrix)
    blankMatrix   = minesweeper.createNewBlankMatrix(preMatrix)

    return render_template('base.html', tile_grid=preMatrix)


@app.route('/reveal', methods=["POST"])
def revealTile():
    """ Reveal the selected tile. """
    # reveal the tile and neighbors
    # check to make sure game stil going
    print 'made it into reveal'
    return jsonify({'confirm': True})


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
