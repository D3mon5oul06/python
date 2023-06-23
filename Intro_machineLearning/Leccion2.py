#ejercicio 1
# print the list of columns in the dataset to find the name of the prediction target
print(home_data.columns)

y = home_data['SalePrice']

#ejercicio 2
# Create the list of features
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

#ejercicio 3
# Print description or statistics from X
print(X.describe())

# Print the top few lines of X
print(X.head())

# Import the necessary module
from sklearn.tree import DecisionTreeRegressor

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=42)  # Set random_state for reproducibility

# Fit the model
iowa_model.fit(X, y)

#ejercicio 4
# Make predictions
predictions = iowa_model.predict(X)

# Print the predictions
print(predictions)


