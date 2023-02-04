# import modules
import os,csv

# function exports movie objects to csv
# takes list of movie objects, filename and list of objects attributes 

def movies_to_csv(my_movies,file_name,attr):
    path = os.path.join(os.getcwd(),file_name+'.csv')
    f = open(path, 'w', encoding='UTF8', newline='')
    writer = csv.writer(f)  
    writer.writerow(attr)
    rows = [[movie.get(attr_i,None) for attr_i in attr] 
            for movie in my_movies]
    writer.writerows(rows)     
    f.close()
    
# function exports movies vote details to csv
# takes list of movie objects, file_name
def movies_vote_to_csv(my_movies,file_name): 
# construct header
    votes = [key+' votes' for key in my_movies[0]['demographics'].keys()]
    rating = [key+' rating' for key in my_movies[0]['demographics'].keys()]
    number_of_votes =  my_movies[0]['number of votes'].keys()
    header = votes+rating+list(number_of_votes)
# write header
    path = os.path.join(os.getcwd(),file_name+'.csv')
    f = open(path, 'w', encoding='UTF8', newline='')
    writer = csv.writer(f)  
    writer.writerow(['imdbID']+header)
# construct and write row
    for movie in my_movies:
        row_votes = [movie['demographics'][key]['votes'] 
               for key in movie['demographics'].keys()]
        row_rating = [movie['demographics'][key]['rating'] 
         for key in movie['demographics'].keys()]
        row_number_of_votes = [movie['number of votes'][key]
          for key in movie['number of votes'].keys()]
        writer.writerow([movie.getID()]+row_votes+row_rating
                        +row_number_of_votes)
    f.close()
    
   


    
 
    
 
   