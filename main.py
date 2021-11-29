import pandas as pd
import numpy as np
import random

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

movies = movies[['movieId', 'title']]
ratings = ratings[['userId','movieId','rating']]

list_titulos = movies['title'].tolist()
list_moviesID = movies['movieId'].tolist()

movies = {}

for t, m in zip(list_titulos, list_moviesID):
    movies[m] = t

randomMovies = random.sample(movies.items(), 4)

valoraciones = []

userID = ratings['userId'].tolist()
userID = userID[-1] + 1

for movie in randomMovies:
    valoracion = input("Introduce valoriación de la pelicula " + movie[1] + "\n")
    rating = Rating(userID,movie[0],valoracion) 
    valoraciones.append(rating)


for v in valoraciones:
    print(v)



#PEARSON

user_rating = {}

#






