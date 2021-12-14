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

movies = movies[['movieId', 'title']]
ratings = ratings[['userId','movieId','rating']]

list_titulos = movies['title'].tolist()
list_moviesID = movies['movieId'].tolist()

movies = {}

for t, m in zip(list_titulos, list_moviesID):
    movies[m] = t

randomMovies = random.sample(movies.items(), 4)

valoraciones = []

userlist = ratings['userId'].tolist()
userID = userlist[-1] + 1

userset = set(userlist);

total = 0

for movie in randomMovies:
    valoracion = input("Introduce valoriación de la pelicula " + movie[1] + "\n")
    rating = Rating(userID,movie[0],valoracion) 
    valoraciones.append(rating)
    total += int(valoracion)

media_actual = total/len(randomMovies)


for v in valoraciones:
    print(v)


for i in range(1,max(userlist)+1,1):
    user_rating = ratings.groupby(ratings.userId).get_group(i)
    media = user_rating['rating'].mean()
    
    for r in randomMovies:
        for u in user_rating.items():
            if r[0] in user_rating.movieId:
                #tmp = user_rating.loc[user_rating["movieId"]== r[0], ["rating"]]
                #print(tmp)
                print(u[1])

            

    #print(user_rating)
    




