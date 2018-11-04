import pandas as pd
import numpy as np


data= pd.read_csv('movies.csv');
print('Shape of data.csv: {}'.format(data.shape));

print ("Total no. of Movies: {}".format(data.shape[0]));

ratings_data=pd.read_csv('ratings.csv');
print('Shape of ratings.csv: {}'.format(ratings_data.shape));
print(ratings_data.describe());

print ("Minimum rating: {}".format(ratings_data['rating'].min()));
print ("Maximum rating: {}".format(ratings_data['rating'].max()));

del ratings_data['timestamp'];
merged_data=data.merge(ratings_data,on = 'movieId',how = 'inner');
print(merged_data.head(3))
high=most_rated = merged_data.groupby('title').size().sort_values(ascending=False)[:25]
most_rated.head(25);
print(high)

#print(data.head);

# drama_movies=data['genres'].str.contains('Drama');
# #print(data[drama_movies].shape)
# print ("Total no. of Drama Movies: {}".format(data[drama_movies].shape[0]));
# print(data[drama_movies].head())
#
# comedy_movies=data['genres'].str.contains('Comedy');
# #print(data[drama_movies].shape)
# print ("Total no. of Comedy Movies: {}".format(data[comedy_movies].shape[0]));
# print(data[drama_movies].head())

genres_list = pd.DataFrame(data.genres.str.split('|').tolist()).stack().unique()
genres_list=np.array(genres_list);
genres_unique = pd.DataFrame(genres_list, columns=['genre']) # Format into DataFrame to store
print("No. of genres: ")
print(len(genres_list));
print(genres_unique);


#print(genres_list)

def genre_total(genreName):
    list=data['genres'].str.contains(genreName);
    print('Total no. of '+ genreName+ ' Movies: {}'.format(data[list].shape[0]));
    #print(data[list].head());

for genre in genres_list:
    genre_total(genre);
    #print( genre);


