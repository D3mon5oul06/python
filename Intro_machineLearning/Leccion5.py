from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Define the model. Set random_state to 1
rf_model = RandomForestRegressor(random_state=1)

# Fit the model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of your Random Forest model on the validation data
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Random Forest Validation MAE: {:,.0f}".format(rf_val_mae))