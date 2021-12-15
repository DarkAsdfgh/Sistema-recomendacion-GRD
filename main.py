import pandas as pd
import numpy as np
import random

from scipy import stats

np.seterr('ignore')
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

movies = movies[['movieId', 'title']]
list_titulos = movies['title'].tolist()
# print(random.sample(list_titulos, 20))
class Movie:
    def __init__(self, movieId, title):
        self.movieId = movieId
        self.title = title

class Rating:
    def __init__(self, userId, movieId, rating):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating

    def __str__(self):
        return "Usuario: " + str(self.userId) + "\n" + "ID: " + str(self.movieId) + "\n" + "Rating: " + str(self.rating) + "\n" 

ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")
movies.set_index("movieId")

movies = movies[['movieId', 'title']]
ratings = ratings[['userId','movieId','rating']]

list_titulos = movies['title'].tolist()
list_moviesID = movies['movieId'].tolist()

randomMovies = movies.sample(20)

print(randomMovies)

valoraciones = []

userlist = ratings['userId'].tolist()
userID = userlist[-1] + 1

userset = set(userlist);

total = 0

for movie in randomMovies.itertuples():
    valoracion = input("Introduce valoración de la pelicula " + str(movie[2]) + "\n")
    rating = Rating(userID,movie[1],valoracion) 
    valoraciones.append(float(valoracion))
    total += int(valoracion)

media_actual = total/len(randomMovies)

vecinos = {}

for i in range(1,max(userlist)+1,1):
    puntuaciones = []
    user_rating = ratings.groupby(ratings.userId).get_group(i)
    media = user_rating['rating'].mean()
    
    for r in randomMovies.itertuples():
        if r[1] in user_rating.movieId.values:
            tmp = user_rating.loc[user_rating['movieId'] == r[1], ['rating']]
            tmp = float(tmp.iloc[0]['rating'])
            puntuaciones.append(tmp)
        else:
            puntuaciones.append(float(0))

    correlacion = stats.mstats.pearsonr(valoraciones, puntuaciones)[0]
    if np.isnan(correlacion):
        correlacion = 0
    vecinos[i] = correlacion

vecinos = sorted(vecinos.items(), key=lambda x:x[1], reverse=True)[:10]
print("Los 10 vecinos más próximos son los siguientes:")
for key, value in vecinos:
    print(str(key) + ": " + str(value))