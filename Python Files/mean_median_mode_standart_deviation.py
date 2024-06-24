import pandas as pd
import numpy as np

file_path = r"C:\Users\yasin\Desktop\Ülkeler\countries.csv"
df = pd.read_csv(file_path)

Selected_foods = df[(df['commodity'] == 'Tomatoes') & (df['Country'] == 'Kyrgyzstan')]

mean_temperature = np.mean(Selected_foods['averageTemperature'])
median_temperature = np.median(Selected_foods['averageTemperature'])
mode_temperature = Selected_foods['averageTemperature'].mode().iat[0]
std_dev_temperature = np.std(Selected_foods['averageTemperature'])

print(f"Mean Temperature: {mean_temperature:.2f} °C")
print(f"Median Temperature: {median_temperature:.2f} °C")
print(f"Mode Temperature: {mode_temperature:.2f} °C")
print(f"Standard Deviation: {std_dev_temperature:.2f} °C")
