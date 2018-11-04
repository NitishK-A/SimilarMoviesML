import pandas as pd
import numpy as np


data= pd.read_csv('movies.csv');
print(data.shape);
print ("Total no. of Movies: {}".format(data.shape[0]));
#print(data.head);

drama_movies=data['genres'].str.contains('Drama');
#print(data[drama_movies].shape)
print ("Total no. of Drama Movies: {}".format(data.shape[0]));
print(data[drama_movies].head())
