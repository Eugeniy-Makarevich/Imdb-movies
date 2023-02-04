# import modules
import pickle
from imdb250_func import *    # all functions in dedicated file

# load movie objects from file
with open('top250_imdb', 'rb') as top250_file:
    top250_movies = pickle.load(top250_file)
    
# list of main attributes to export
columns = ['imdbID','original title','year','top 250 rank','rating',
           'runtime', 'box office','metascore','genres']

# export main info to csv
movies_to_csv(top250_movies,'movies_main',columns)

# export additional info
columns = ['imdbID','countries']
movies_to_csv(top250_movies,'movies_misc',columns)

# export vote details
movies_vote_to_csv(top250_movies,'movies_vote_to_csv')



