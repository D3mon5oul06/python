#ejercicio 1:
desc = reviews['description']

#ejercicio 2:
first_description = reviews.loc[0, 'description']

#ejercicio 3: 
first_row = reviews.loc[0]

#ejercicio 4:
first_descriptions = reviews['description'].head(10)

#ejercicio 5:
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]

#ejercicio 6:
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]

#ejercicio 7:
df = reviews.loc[:99, ['country', 'variety']]

#ejercicio 8:
italian_wines = reviews[reviews['country'] == 'Italy']

#ejercicio 9:
top_oceania_wines = reviews[(reviews['points'] >= 95) & ((reviews['country'] == 'Australia') | (reviews['country'] == 'New Zealand'))]
