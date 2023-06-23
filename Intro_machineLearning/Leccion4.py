#ejercicio 1
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
best_mae = float('inf')  # Initialize with a large value
best_tree_size = None

# Loop through each value of max_leaf_nodes
for max_leaf_nodes in candidate_max_leaf_nodes:
    # Calculate the MAE for the current max_leaf_nodes value
    mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    
    # Check if the current MAE is better than the best MAE so far
    if mae < best_mae:
        best_mae = mae
        best_tree_size = max_leaf_nodes

# Print the best value of max_leaf_nodes
print("Best tree size:", best_tree_size)

#ejercicio 2
# Create the final model with the optimal tree size
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=0)

# Fit the final model using all the data
final_model.fit(X, y)

