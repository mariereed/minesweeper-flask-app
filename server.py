
from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import os


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
    tile_grid = [[1,2,3,0,0,0,0,0],
    			 [4,5,6,0,0,0,0,0],
    			 [7,8,9,0,0,0,0,0],
    			 [10,11,12,0,0,0,0,0],
    			 [0,0,0,0,0,0,0,0],
    			 [0,0,0,0,0,0,0,0],
    			 [0,0,0,0,0,0,0,0],
    			 [0,0,0,0,0,0,0,0]]

    return render_template('base.html', tile_grid=tile_grid)


if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    app.debug = True
    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
