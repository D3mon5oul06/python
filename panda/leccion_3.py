#ejercicio 1:
median_points = reviews['points'].median()

#ejercicio 2:
countries = reviews['country'].unique()

#ejercicio 3:
reviews_per_country = reviews['country'].value_counts()

#ejercicio 4:
centered_price = reviews['price'] - reviews['price'].mean()

#ejercicio 5:
bargain_wine = reviews.loc[(reviews['points'] / reviews['price']).idxmax(), 'title']

#ejercicio 6:
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

#ejercicio 7:
def get_star_rating(row):
    if row['country'] == 'Canada':
        return 3
    elif row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(get_star_rating, axis=1)
