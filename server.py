"""Server for movie ratings app."""

from flask import (Flask, session, render_template, flash, request, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!





@app.route('/')
def homepage():
    """View Homepage"""
    return render_template('homepage.html')


@app.route('/movies')
def movie_page():
    """Display all movies"""

    all_movies = crud.return_all_movies()

    return render_template('movies.html', movies=all_movies)



@app.route('/users')
def user_page():
    """Display all Users"""

    users = crud.return_all_users()
    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Gives info on a Specific User"""
    user_details = crud.get_user_by_id(user_id)

    return render_template('user_details.html',user=user_details)




@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Give Info on a Specific Movie"""
    movie_details = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html',movie=movie_details)





if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

