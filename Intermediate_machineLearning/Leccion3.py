#ejercicio 1
# Drop columns in training data
drop_X_train = X_train.select_dtypes(exclude=['object'])

# Drop columns in validation data
drop_X_valid = X_valid.select_dtypes(exclude=['object'])

#ejercicio 2
from sklearn.preprocessing import OrdinalEncoder

# Drop categorical columns that will not be encoded
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)

# Apply ordinal encoder
encoder = OrdinalEncoder()
label_X_train[good_label_cols] = encoder.fit_transform(label_X_train[good_label_cols])
label_X_valid[good_label_cols] = encoder.transform(label_X_valid[good_label_cols])

#ejercicio 3
# Fill in the line below: How many categorical variables in the training data have cardinality greater than 10?
high_cardinality_numcols = 3

# Fill in the line below: How many columns are needed to one-hot encode the 'Neighborhood' variable in the training data?
num_cols_neighborhood = 25

#ejercicio 4
# Fill in the line below: How many entries are added to the dataset by 
# replacing the column with a one-hot encoding?
OH_entries_added = 10000 * (100 - 1)

# Fill in the line below: How many entries are added to the dataset by
# replacing the column with an ordinal encoding?
label_entries_added = 0

#ejercicio 5
from sklearn.preprocessing import OneHotEncoder

# Use as many lines of code as you need!

# Instantiate the OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

# One-hot encode the categorical columns in low_cardinality_cols for X_train
OH_X_train = pd.DataFrame(encoder.fit_transform(X_train[low_cardinality_cols]))
OH_X_train.index = X_train.index

# One-hot encode the categorical columns in low_cardinality_cols for X_valid
OH_X_valid = pd.DataFrame(encoder.transform(X_valid[low_cardinality_cols]))
OH_X_valid.index = X_valid.index

# Check the remaining non-categorical columns in X_train and X_valid
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

# Concatenate the one-hot encoded and numerical columns for X_train
OH_X_train = pd.concat([OH_X_train, num_X_train], axis=1)

# Concatenate the one-hot encoded and numerical columns for X_valid
OH_X_valid = pd.concat([OH_X_valid, num_X_valid], axis=1)
