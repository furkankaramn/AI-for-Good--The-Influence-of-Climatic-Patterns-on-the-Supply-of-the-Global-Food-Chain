import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

merged_file_path = r"C:/Users/Monster/Desktop/countries.csv"
df = pd.read_csv(merged_file_path)

filtered_df = df[(df['commodity'] == 'Potatoes') & (df['Country'] == 'Yemen')]

# Convert 'date' column to datetime
filtered_df['date'] = pd.to_datetime(filtered_df['date'], errors='coerce')

monthly_avg_price = filtered_df.groupby('date')['usdprice'].mean().reset_index()

plt.figure(figsize=(10, 6))

plt.plot(filtered_df['date'], filtered_df['windStrength'], label='Wind Strength', marker='o')
plt.plot(filtered_df['date'], filtered_df['averageTemperature'], label='Average Temperature', marker='o')

plt.plot(monthly_avg_price['date'], monthly_avg_price['usdprice'], label='Monthly Avg Price', linestyle='--', color='black', marker='o')

plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Monthly Avg Price and Weather for Potatoes in Yemen')

# Format dates on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b '))

plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

