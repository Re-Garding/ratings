"""Drop and ReCreate tables with practice data"""

import os, json, crud, model, server
from random import choice, randint
from datetime import datetime

os.system('dropfb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    title, overview, poster_path = (
        movie["title"],
        movie["overview"],
        movie["poster_path"],
    )
    
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)




for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    new_user = crud.create_user(email, password)
    
    for n in range(10):
        movie = choice(movies_in_db)
        rate = randint(1, 5)
        crud.create_rating(new_user.user_id, movie.movie_id, rate)