import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

csv_file_path = r"C:\Users\Monster\Desktop\countries.csv"

df = pd.read_csv(csv_file_path, parse_dates=['date'])
df['date'] = pd.to_datetime(df['date'], errors='coerce')

df = df.dropna(subset=['date', 'averageTemperature'])

plt.figure(figsize=(12, 6))

colors = plt.cm.viridis_r(df['date'].dt.month / 12)

plt.scatter(df['date'], df['averageTemperature'], label='Monthly Average Temperature', color=colors, alpha=0.7)

plt.xlabel('Date')
plt.ylabel('Average Temperature')
plt.title('Monthly Average Temperature Scatter Plot')

plt.xticks(df['date'].unique(), df['date'].dt.strftime('%b ').unique(), rotation=45, ha='right')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b '))

plt.legend()
plt.tight_layout()

plt.show()