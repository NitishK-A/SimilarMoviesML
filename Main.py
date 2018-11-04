import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data= pd.read_csv('movies.csv');
print('Shape of data.csv: {}'.format(data.shape));
print()

print ("Total no. of Movies: {}".format(data.shape[0]));
print()

ratings_data=pd.read_csv('ratings.csv');
print('Shape of ratings.csv: {}'.format(ratings_data.shape));
print()
print(ratings_data.describe());
print()

print ("Minimum rating: {}".format(ratings_data['rating'].min()));
print ("Maximum rating: {}".format(ratings_data['rating'].max()));
print()

del ratings_data['timestamp'];
merged_data=data.merge(ratings_data,on = 'movieId',how = 'inner');
print("Merged Data:")
print(merged_data.head(3))
print()

#top 25 most rated movies
print("50 Most Rated Movies :")
most_rated = merged_data.groupby('title').size().sort_values(ascending=False)[:50]
print(most_rated)
print()

#Highest rated movies
highest_rated=merged_data.groupby('title')['rating'].mean().sort_values(ascending=False)[:100];
print(highest_rated);
print();






genres_list = pd.DataFrame(data.genres.str.split('|').tolist()).stack().unique()
genres_list=np.array(genres_list);
genres_unique = pd.DataFrame(genres_list, columns=['genre']) # Format into DataFrame to store
print("No. of genres: ")
print(len(genres_list));
print(genres_unique);

def genre_total(genreName):
    list=data['genres'].str.contains(genreName);
    out=data[list].shape[0];
    print('Total no. of '+ genreName+ ' Movies: {}'.format(data[list].shape[0]));
    return out
    #print(data[list].head());
arr=[];

for genre in genres_list:
    o=genre_total(genre);
    arr.append(o);
print(arr)

fig = plt.figure(1, figsize=(55,55))
ax2 = fig.add_subplot(1,1,1)
y_axis = [i for i in arr]
x_axis = [k for k,i in enumerate(genres_list)]
x_label = [i for i in genres_list]
plt.xticks(rotation=90, fontsize = 10)
plt.yticks(fontsize = 15)
plt.xticks(x_axis, x_label)
plt.ylabel("No. of occurences", fontsize = 14, labelpad = 0)
ax2.bar(x_axis, y_axis, color='b')
plt.title("Popularity of Genres")
#plt.show()



