
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

    return render_template('base.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    app.debug = True
    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
