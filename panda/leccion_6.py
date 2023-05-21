#ejercicio 1
dtype = reviews['points'].dtype

#ejercicio 2
point_strings = reviews['points'].astype(str)

#ejercicio 3
n_missing_prices = reviews['price'].isnull().sum()

#ejercicio 4
reviews_per_region = reviews['region_1'].fillna('Unknown').value_counts().sort_values(ascending=False)
