#ejercicio 1:
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})

#ejercicio 2:
reindexed = reviews.rename_axis('wines', axis='rows')

#ejercicio 3:
combined_products = pd.concat([gaming_products, movie_products])

#ejercicio 4:
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
