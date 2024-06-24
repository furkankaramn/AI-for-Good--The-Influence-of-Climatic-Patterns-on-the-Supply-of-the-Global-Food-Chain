import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = r"C:\Users\Monster\Downloads\countries.csv"
df = pd.read_csv(csv_file_path)

column_name = 'averageTemperature'

plt.figure(figsize=(10, 6))
plt.hist(df[column_name], bins=20, color='blue', alpha=0.7)
plt.xlabel(column_name)
plt.ylabel('Frequency')
plt.title(f'Histogram of {column_name}')
plt.grid(True)
plt.show()
