


import pandas as pd
import itertools

df = pd.read_csv("cityspire-c-ds/data/pop_rent_crime_walk_cost_livability_bins.csv")

some_values = "Phoenix, Arizona"

#print(df.loc[df['Location'] == some_values])

#print(df.dtypes)

#print(df.loc[df['Location'] == some_values, '2019 Population'])

#print(df[df['Location']==some_values]['2019 Population'])

print(df.loc[df['Location'] == some_values])