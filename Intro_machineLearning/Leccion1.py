#ejercicio 1
import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Call line below with no argument to check that you've loaded the data correctly
step_1.check()

#ejercicio 2
# Print summary statistics
summary_stats = home_data.describe()
print(summary_stats)

# Calculate average lot size
avg_lot_size = round(home_data['LotArea'].mean())

# Determine the age of the newest home
current_year = 2023  # Replace with the current year
newest_home_age = current_year - home_data['YearBuilt'].max()

