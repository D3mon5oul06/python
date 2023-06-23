#ejercico 1
# Import the train_test_split function
from sklearn.model_selection import train_test_split

# Split the data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

#ejercicio 2
# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data
iowa_model.fit(train_X, train_y)

#ejercicio 3
# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

#inspect predictions 
# Print the top few validation predictions
print(val_predictions[:5])

# Print the top few actual prices from the validation data
print(val_y.head())

#ejercicio 4
from sklearn.metrics import mean_absolute_error

# Calculate the mean absolute error
val_mae = mean_absolute_error(val_y, val_predictions)

# Uncomment the following line to see the validation MAE
print(val_mae)


