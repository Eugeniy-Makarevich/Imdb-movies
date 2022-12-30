import  imdb,pickle 

ia = imdb.Cinemagoer()

# infosets to download
movie_infoset = ['main','awards','critic reviews','vote details']
 
# get top 250 movies IDs and download
top250id =[top_i.movieID for top_i in  ia.get_top250_movies()]
top250_movies = [ia.get_movie(movie_id,info=movie_infoset) 
                 for movie_id in top250id]
# export to file
with open('top250_imdb', 'wb') as top250_imdb_file:
    pickle.dump(top250_movies, top250_imdb_file)