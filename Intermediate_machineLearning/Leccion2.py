#ejercicio 1
# Fill in the line below: How many rows are in the training data?
num_rows = X_train.shape[0]

# Fill in the line below: How many columns in the training data
# have missing values?
num_cols_with_missing = sum(missing_val_count_by_column > 0)

# Fill in the line below: How many missing entries are contained in 
# all of the training data?
tot_missing = missing_val_count_by_column.sum()

#ejercicio 2
# Get names of columns with missing values
cols_with_missing = X_train.columns[X_train.isnull().any()]

# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

#ejercicio 3
from sklearn.impute import SimpleImputer

# Create an instance of SimpleImputer with strategy='mean'
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on X_train
imputer.fit(X_train)

# Impute missing values in X_train and X_valid
imputed_X_train = pd.DataFrame(imputer.transform(X_train), columns=X_train.columns)
imputed_X_valid = pd.DataFrame(imputer.transform(X_valid), columns=X_valid.columns)

#ejercicio 4
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Create an imputer
imputer = SimpleImputer(strategy='mean')

# Fit and transform the training data
final_X_train = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)

# Transform the validation data
final_X_valid = pd.DataFrame(imputer.transform(X_valid), columns=X_valid.columns)

# Scale the data
scaler = StandardScaler()
final_X_train = pd.DataFrame(scaler.fit_transform(final_X_train), columns=final_X_train.columns)
final_X_valid = pd.DataFrame(scaler.transform(final_X_valid), columns=final_X_valid.columns)

#ejercicio 5
# Preprocess test data
final_X_test = pd.DataFrame(imputer.transform(X_test), columns=X_test.columns)

# Generate test predictions
preds_test = model.predict(final_X_test)