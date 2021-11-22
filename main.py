import pandas as pd
import numpy as np
import random


ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

movies = movies[['movieId', 'title']]
list_titulos = movies['title'].tolist()
print(random.sample(list_titulos, 20))
class Movie:
    def __init__(self, movieId, title):
        self.movieId = movieId
        self.title = title

class Rating:
    def __init__(self, userId, movieId, rating):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating