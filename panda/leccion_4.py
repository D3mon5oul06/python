#ejercicio 1
reviews_written = reviews.groupby('taster_twitter_handle').size()

#ejercicio 2:
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

#ejercicio 3:
price_extremes = reviews.groupby('variety')['price'].agg(['min', 'max'])

#ejercicio 4:
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

#ejercicio 5:
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()

#ejercicio 6:
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
