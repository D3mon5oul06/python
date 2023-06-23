#ejercicio 1
from xgboost import XGBRegressor

# Define the model
my_model_1 = XGBRegressor(random_state=0)

# Fit the model
my_model_1.fit(X_train, y_train)

#ejercicio 2
from sklearn.metrics import mean_absolute_error

# Get predictions
predictions_1 = my_model_1.predict(X_valid)

#ejercicio 3
from sklearn.metrics import mean_absolute_error

# Calculate MAE
mae_1 = mean_absolute_error(y_valid, predictions_1)

# Uncomment to print MAE
print("Mean Absolute Error:", mae_1)

#ejercicio 4
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

# Define the model with modified parameters
my_model_2 = XGBRegressor(n_estimators=1000, learning_rate=0.05, random_state=0)  # Modify the parameters as desired

# Fit the model
my_model_2.fit(X_train, y_train)

# Get predictions
predictions_2 = my_model_2.predict(X_valid)

# Calculate MAE
mae_2 = mean_absolute_error(y_valid, predictions_2)

# Uncomment to print MAE
print("Mean Absolute Error:", mae_2)

#ejercicio 5
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

# Define the model with modified parameters
my_model_3 = XGBRegressor(n_estimators=10, learning_rate=0.2, random_state=0)  # Modify the parameters as desired

# Fit the model
my_model_3.fit(X_train, y_train)

# Get predictions
predictions_3 = my_model_3.predict(X_valid)

# Calculate MAE
mae_3 = mean_absolute_error(y_valid, predictions_3)

# Uncomment to print MAE
print("Mean Absolute Error:", mae_3)
