#!/usr/bin/env python
# coding: utf-8

# In[12]:


# In this Jupyter Notebook we will be choosing six recent popular movies and ask at least five people that we  know  to rate each of these movies that they have seen on a scale of 1 to 5. Based off those answers we will be performing a few tasks with this data. 
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

#Reading the movie rating information from the csv file into pandas
movie_rating = pd.read_csv(r'C:\Users\Sixpm\Downloads\Movies.csv')

#Showing the average ratings for each user and each movie.
movie_rating_copy = movie_rating.copy()
movie_rating_copy['Friend Average Rating'] = movie_rating_copy.mean(axis=1)
movie_rating_copy
average_score = movie_rating_copy[0:4].mean()
average_score = movie_rating_copy.append(average_score, ignore_index=True)
average_score.loc[5,'Friends']="Average Movie Rating"
average_score
zscore = lambda x: (x - x.mean()) / x.std()


#Creating a new pandas dataframe, with normalized ratings for each user. Again, showing the average ratings for each user and each movie.
normalized = movie_rating.copy()
normalized
cols_to_norm = ["Spider-Man: No Way Home", "Shazam ", "Joker", "The Batman ", "Dune", "Knives Out"]
normalized[cols_to_norm] =scaler.fit_transform(normalized[cols_to_norm])
normalized 


normalized_copy = normalized.copy()
normalized_copy['Friend Average Rating'] = normalized_copy.mean(axis=1)
normalized_copy

#There are advantages and disadvantages to using of using normalized ratings instead of the actual ratings. An advantage to using normalized ratings is for ease of graphing the data set. Another would be that it scales all values within the range [0,1] which makes it very easy to work with the data. As well as the fact that normalization eliminates the duplicate data.
# A disadvantage of using normalized ratings would be that careless/improper use of normalization may lead to terrible design filled with major anomalies and data inconsistency.

#[Extra credit] Create another new pandas dataframe, with standardized ratings for each user. Once again, show the average ratings for each user and each movie.

standardized = normalized[cols_to_norm].apply(zscore)
standardized
average_score=standardized[0:4].mean()
average_score=standardized.append(average_score, ignore_index=True)
average_score['Friend Average Rating'] = average_score.mean(axis=1)
average_score


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




