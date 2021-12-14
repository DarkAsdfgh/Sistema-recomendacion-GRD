import pandas as pd
import numpy as np
import random


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

randomMovies = movies.sample(4)

print(randomMovies)

valoraciones = []

userlist = ratings['userId'].tolist()
userID = userlist[-1] + 1

userset = set(userlist);

total = 0

for movie in randomMovies.itertuples():
    valoracion = input("Introduce valoración de la pelicula " + str(movie[2]) + "\n")
    rating = Rating(userID,movie[1],valoracion) 
    valoraciones.append(rating)
    total += int(valoracion)

media_actual = total/len(randomMovies)

for v in valoraciones:
    print(v)


for i in range(1,max(userlist)+1,1):
    user_rating = ratings.groupby(ratings.userId).get_group(i)
    media = user_rating['rating'].mean()
    
    for r in randomMovies.itertuples():
        if r[1] in user_rating.movieId.values:
            print("Usuario " + str(i) + "\tPelícula " + r[2])
            tmp = user_rating.loc[user_rating['movieId'] == r[1], ['rating']].values
            print(tmp)


            

    #print(user_rating)