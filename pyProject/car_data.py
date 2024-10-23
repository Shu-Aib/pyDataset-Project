import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use raw string for the file path to avoid issues with backslashes
file_path = r'C:\Users\shubs\Desktop\pyProject\USA_cars_datasets.csv'

# Try to load the CSV file into a pandas DataFrame
try:
    cars_data = pd.read_csv(file_path)
    print("File loaded successfully!")
except FileNotFoundError:
    print(f"File not found. Please check the path: {file_path}")
    raise

# Display basic information about the dataset (columns, data types, memory usage)
print(cars_data.info())

# Show summary statistics for numerical columns
print(cars_data.describe())

# Remove duplicate rows from the dataset
cars_data = cars_data.drop_duplicates()

# Remove rows with missing data (NaN values)
cars_data = cars_data.dropna()

# Show descriptive statistics again after cleaning the data
print(cars_data.describe())

# Create a histogram to show the distribution of car prices
plt.figure(figsize=(10, 6))
sns.histplot(cars_data['price'], bins=30, kde=True)  # kde=True adds a density estimate
plt.title('Price Distribution')  # Add a title
plt.xlabel('Price')  # Label x-axis
plt.ylabel('Frequency')  # Label y-axis
plt.show()  # Display the plot

# Create a histogram to show the distribution of car years
plt.figure(figsize=(10, 6))
sns.histplot(cars_data['year'], bins=30, kde=True)
plt.title('Year Distribution')  # Add a title
plt.xlabel('Year')  # Label x-axis
plt.ylabel('Frequency')  # Label y-axis
plt.show()

# Create a histogram to show the distribution of car mileage
plt.figure(figsize=(10, 6))
sns.histplot(cars_data['mileage'], bins=30, kde=True)
plt.title('Mileage Distribution')  # Add a title
plt.xlabel('Mileage')  # Label x-axis
plt.ylabel('Frequency')  # Label y-axis
plt.show()

# Create a scatter plot to show the relationship between mileage and price
# Hue colors the points by car year
plt.figure(figsize=(10, 6))
sns.scatterplot(data=cars_data, x='mileage', y='price', hue='year', palette='coolwarm', alpha=0.7)
plt.title('Price vs Mileage with Year Hue')  # Add a title
plt.xlabel('Mileage')  # Label x-axis
plt.ylabel('Price')  # Label y-axis
plt.show()

# Group the data by car brand and calculate the average price, mileage, and the count of cars
brand_analysis = cars_data.groupby('brand').agg(
    avg_price=('price', 'mean'),      # Calculate average price
    avg_mileage=('mileage', 'mean'),  # Calculate average mileage
    car_count=('brand', 'count')      # Count the number of cars per brand
).sort_values(by='avg_price', ascending=False)  # Sort brands by average price

# Print the brand analysis table
print(brand_analysis)

# Group the data by year and calculate the average price and mileage
year_analysis = cars_data.groupby('year').agg(
    avg_price=('price', 'mean'),      # Calculate average price
    avg_mileage=('mileage', 'mean')   # Calculate average mileage
).sort_index()  # Sort by year in ascending order

# Print the yearly analysis table
print(year_analysis)

# Create a line plot to show the trend of average price over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=year_analysis, x=year_analysis.index, y='avg_price')
plt.title('Average Price by Year')  # Add a title
plt.xlabel('Year')  # Label x-axis
plt.ylabel('Average Price')  # Label y-axis
plt.show()

# Create a line plot to show the trend of average mileage over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=year_analysis, x=year_analysis.index, y='avg_mileage')
plt.title('Average Mileage by Year')  # Add a title
plt.xlabel('Year')  # Label x-axis
plt.ylabel('Average Mileage')  # Label y-axis
plt.show()
