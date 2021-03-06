
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, session, jsonify
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
    height = session.get('height') or 8
    width = session.get('width') or 8
    mine_count = session.get('mine_count') or 10

    true_false_matrix      = minesweeper.create_true_false_matrix(height, width, mine_count)
    number_and_mine_matrix = minesweeper.number_fill(true_false_matrix)
    blank_matrix           = minesweeper.create_new_blank_matrix(true_false_matrix)

    session['number_and_mine_board'] = number_and_mine_matrix
    session['current_board'] = blank_matrix

    return render_template('base.html', tile_grid=true_false_matrix, mine_count=mine_count)


@app.route('/reveal', methods=["POST"])
def revealTile():
    """ Reveal the selected tile. """

    full_board    = session.get('number_and_mine_board')
    current_board = session.get('current_board')

    x, y = eval(request.form.get('coordinates'))
    was_revealed, board = minesweeper.reveal_click(x, y, full_board, current_board)

    session['current_board'] = board

    if was_revealed:
        return jsonify({'confirm': True, 'board': board, 'gameOver': minesweeper.game_over(board, full_board)})
    else:
        return jsonify({'confirm': False, 'board': board})


@app.route('/flag', methods=["POST"])
def flagTile():
    """ Reveal the selected tile. """
    x, y = eval(request.form.get('coordinates'))

    return jsonify({'confirm': True, 'x': x, 'y': y})


@app.route('/mode', methods=["POST"])
def changeMode():
    """ Reveal the selected tile. """
    mode = request.form.get('mode')

    if mode == 'beginner':
        height     = 8
        width      = 8
        mine_count = 10
    elif mode == 'intermediate':
        height     = 16
        width      = 16
        mine_count = 40
    elif mode == 'advanced':
        height     = 16
        width      = 30
        mine_count = 99

    session['height']     = height
    session['width']      = width
    session['mine_count'] = mine_count

    return ''


if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # app.debug = True

    app.run(port=5000, host='0.0.0.0')
