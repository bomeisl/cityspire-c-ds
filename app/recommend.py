#app/ecommend.py



# Imports

from os import path
import pandas as pd
import pickle
import json


# Load pickled vectorizer and model

with open('./pickles/tfidf.pkl', 'rb') as tfidf_pkl:
    tfidf = pickle.load(tfidf_pkl)

with open('./pickles/nn_model.pkl', 'rb') as nn_pkl:
    nn_model = pickle.load(nn_pkl)

#with open('./pickles/min_data.pkl', 'rb') as data_pkl:
#    data = pickle.load(data_pkl)
"""Pickle data to use here, or try loading from DB"""


# Import pop_rent_crime_bins csv

file_name = path.join(path.dirname(__file__), "../data/pop_rent_crime_bins.csv")

prcb = pd.read_csv(file_name)


# Recommend Function

def recommend(user_input):
    temp_df = nn_model.kneighbors(tfidf.transform([user_input]).todense())[1]

    for i in range(4):
        info = prcb.iloc[temp_df[0][i]]['Location']
        info_pop = prcb.iloc[temp_df[0][i]]['2019 Population']
        info_town_or_city = prcb.iloc[temp_df[0][i]]['Town or City']
        info_rent = prcb.iloc[temp_df[0][i]]['2019 Rental Rates']
        info_state = prcb.iloc[temp_df[0][i]]['State']
        info_city = prcb.iloc[temp_df[0][i]]['City']
        info_population = prcb.iloc[temp_df[0][i]]['Population']
        info_violent_crime = prcb.iloc[temp_df[0][i]]['Violent crime']
        info_murder = prcb.iloc[temp_df[0][i]]['Murder and nonnegligent manslaughter']
        info_vehicle_theft = prcb.iloc[temp_df[0][i]]['Motor vehicle theft']
        info_arson = prcb.iloc[temp_df[0][i]]['Arson']
        info_crime_rate = prcb.iloc[temp_df[0][i]]['Crime Rate']
        info_urb_pop_cat = prcb.iloc[temp_df[0][i]]['Urban Population by City Size Categories']
        info_urb_pop_rang = prcb.iloc[temp_df[0][i]]['Urban Population by City Size Ranges']
        info_rent_cat = prcb.iloc[temp_df[0][i]]['Rental Rate Categories']
        info_rent_rang = prcb.iloc[temp_df[0][i]]['Rental Rate Ranges']
        info_crime_cat = prcb.iloc[temp_df[0][i]]['Crime Rate Categories']
        info_crime_rang = prcb.iloc[temp_df[0][i]]['Crime Rate Categories']
        
        # Possible Outputs

        location = json.dumps(info)
        pop = json.dumps(int(info_pop))
        town_or_city = json.dumps(info_town_or_city)
        rent = json.dumps(int(info_rent))
        state = json.dumps(info_state)
        city = json.dumps(info_city)
        population = json.dumps(int(info_population))
        violent_crime = json.dumps(int(info_violent_crime))
        murder = json.dumps(int(info_murder))
        vehicle_theft = json.dumps(int(info_vehicle_theft))
        arson = json.dumps(int(info_arson))
        crime_rate = json.dumps(int(info_crime_rate))
        urb_pop_cat = json.dumps(info_urb_pop_cat)
        urb_pop_rang = json.dumps(info_urb_pop_rang)
        rent_cat = json.dumps(info_rent_cat)
        rent_rang = json.dumps(info_rent_rang)
        crime_cat = json.dumps(info_crime_cat)
        crime_rang = json.dumps(info_crime_rang)

    # Add all future column names

        return [location, pop, town_or_city, rent, state, city, population, violent_crime, murder, vehicle_theft, 
                arson, crime_rate, urb_pop_cat, urb_pop_rang, rent_cat, rent_rang, crime_cat, crime_rang]
