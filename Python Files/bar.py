import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

merged_file_path = r"C:/Users/Monster/Desktop/countries.csv"
df = pd.read_csv(merged_file_path)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

filtered_df = df[(df['commodity'] == 'Potatoes') & (df['Country'] == 'Yemen')]

monthly_avg_price = filtered_df.groupby('date')['usdprice'].mean().reset_index()
monthly_avg_temperature = filtered_df.groupby('date')['averageTemperature'].mean().reset_index()
monthly_avg_wind = filtered_df.groupby('date')['windStrength'].mean().reset_index()

plt.figure(figsize=(12, 6))

bar_width = 0.3

bar_positions_price = range(len(monthly_avg_price['date']))
bar_positions_temperature = [pos + bar_width for pos in bar_positions_price]
bar_positions_wind = [pos + 2 * bar_width for pos in bar_positions_price]

plt.bar(bar_positions_price, monthly_avg_price['usdprice'], width=bar_width, label='Monthly Avg Price', alpha=0.7)
plt.bar(bar_positions_temperature, monthly_avg_temperature['averageTemperature'], width=bar_width, label='Monthly Avg Temperature', alpha=0.7)
plt.bar(bar_positions_wind, monthly_avg_wind['windStrength'], width=bar_width, label='Monthly Avg Wind', alpha=0.7)

plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Monthly Avg Price, Avg Temperature, and Avg Wind for Potatoes in Yemen')

# Format dates on the x-axis
date_labels = monthly_avg_price['date'].dt.strftime('%b').unique()
plt.xticks([pos + bar_width for pos in bar_positions_price], date_labels, rotation=45, ha='right')

plt.legend()

plt.tight_layout()
plt.show()
