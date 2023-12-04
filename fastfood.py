import pandas as pd
import matplotlib.pyplot as plt

# Read data from food.xlsx
food_data = pd.read_excel("food.xlsx")

# Check if "Weight Watchers Pnts" column exists before dropping it
if "Weight Watchers Pnts" in food_data.columns:
    food_data = food_data.drop(columns=["Weight Watchers Pnts"])

# Read data from run.xlsx
run_data = pd.read_excel("run.xlsx")

# Calculate calories burned per hour
run_data['Calories Burned per Hour'] = run_data['Calories Burned'] / run_data['Distance (in miles)']

# Convert "Calories" column to numeric, setting errors='coerce' to handle non-numeric values
food_data["Calories"] = pd.to_numeric(food_data["Calories"], errors="coerce")

# Find the unhealthiest food from each fast-food store
unhealthiest_foods = food_data.loc[food_data.groupby("Company")["Calories"].idxmax()]

# Calculate the burn-off time in hours for each unhealthiest food
unhealthiest_foods["Burn Off Time (hours)"] = unhealthiest_foods["Calories"] / run_data['Calories Burned per Hour'].max()

# Create a DataFrame with the calculated burn-off time
burn_off_time_df = unhealthiest_foods[["Company", "Item", "Burn Off Time (hours)"]]

# Display the DataFrame
print("Burn Off Time DataFrame:")
print(burn_off_time_df)

# Create a scatter plot
plt.scatter(unhealthiest_foods["Calories"], unhealthiest_foods["Burn Off Time (hours)"])
plt.xlabel('Calories in Food')
plt.ylabel('Burn Off Time (hours)')
plt.title('Relationship between Calories in Food and Burn Off Time')
plt.show()

# Count the number of foods from each restaurant with over 1000 calories
foods_over_1000_calories = food_data[food_data["Calories"] > 1000]
restaurant_counts = foods_over_1000_calories["Company"].value_counts()

# Create a DataFrame with the number of foods over 1000 calories from each restaurant
foods_over_1000_df = pd.DataFrame({"Company": restaurant_counts.index, "Number of Foods > 1000 Calories": restaurant_counts})

# Display the DataFrame
print("\nFoods with > 1000 Calories from Each Restaurant:")
print(foods_over_1000_df)

# Create a bar chart
plt.bar(foods_over_1000_df["Company"], foods_over_1000_df["Number of Foods > 1000 Calories"])
plt.xlabel('Restaurant')
plt.ylabel('Number of Foods > 1000 Calories')
plt.title('Number of Foods with > 1000 Calories from Each Restaurant')
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better visibility
plt.show()

# Create a line chart
plt.plot(run_data['Distance (in miles)'], run_data['Calories Burned'], marker='o', linestyle='-')
plt.xlabel('Distance (in miles)')
plt.ylabel('Calories Burned')
plt.title('Calories Burned vs Distance')
plt.grid(True)
plt.show()
