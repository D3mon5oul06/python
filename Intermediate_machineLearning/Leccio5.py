#ejercicio 1
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score

def get_score(n_estimators):
    """Return the average MAE over 3 CV folds of random forest model.
    
    Keyword argument:
    n_estimators -- the number of trees in the forest
    """
    # Create the pipeline
    my_pipeline = Pipeline(steps=[
        ('preprocessor', SimpleImputer()),
        ('model', RandomForestRegressor(n_estimators=n_estimators, random_state=0))
    ])
    
    # Calculate the negative MAE scores using cross-validation
    scores = -1 * cross_val_score(my_pipeline, X, y, cv=3, scoring='neg_mean_absolute_error')
    
    # Return the average MAE score
    return scores.mean()

#ejercicio 2
results = {}

# Evaluate the model performance for different values of n_estimators
for n in range(50, 401, 50):
    scores = -1 * cross_val_score(my_pipeline.set_params(model__n_estimators=n), X, y, cv=3, scoring='neg_mean_absolute_error')
    results[n] = scores.mean()
    
#ejercicio 3
n_estimators_best = min(results, key=results.get)