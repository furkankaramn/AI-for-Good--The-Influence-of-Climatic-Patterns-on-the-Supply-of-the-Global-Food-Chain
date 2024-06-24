import pandas as pd
from scipy.stats import shapiro

csv_file_path = r"C:\Users\Monster\Downloads\countries.csv"

df = pd.read_csv(csv_file_path, parse_dates=['date'])
df['date'] = pd.to_datetime(df['date'], errors='coerce')

df = df.dropna(subset=['date', 'averageTemperature'])

selected_product = 'Tomatoes'
selected_country = 'Kyrgyzstan'
filtered_df = df[(df['commodity'] == selected_product) & (df['Country'] == selected_country)]

temperature_data = filtered_df['averageTemperature']

stat, p_value = shapiro(temperature_data)

print(f'Statistic: {stat}, p-value: {p_value}')

if p_value > 0.05:
    print('The data has a normal distribution.')
else:
    print('The data is not normally distributed.')
