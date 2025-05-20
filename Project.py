import matplotlib.pyplot as plt
import pandas as pd

# Simulated data for urban planning
years = list(range(2015, 2025))
population = [10000, 11000, 12000, 13000, 14000, 15200, 16500, 17900, 19300, 20800]

land_use = {
    'Zone': ['Residential', 'Commercial', 'Industrial', 'Green Space', 'Institutional'],
    'Area (%)': [45, 20, 15, 10, 10]
}

# Create line chart: Population Growth
plt.figure(figsize=(10, 5))
plt.plot(years, population, marker='o', color='teal', linestyle='--')
plt.title('Population Growth Over Years')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.tight_layout()
plt.show()

# Create bar chart: Land Use Distribution
land_df = pd.DataFrame(land_use)
plt.figure(figsize=(8, 5))
plt.bar(land_df['Zone'], land_df['Area (%)'], color='skyblue', edgecolor='black')
plt.title('Land Use Distribution')
plt.xlabel('Land Use Zone')
plt.ylabel('Area (%)')
plt.tight_layout()
plt.show()
