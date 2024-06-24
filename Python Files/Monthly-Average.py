import pandas as pd

csv_file_name = "C:/Users/Monster/Desktop/Weather/Sana.csv"

data = pd.read_csv(csv_file_name)

data['date'] = pd.to_datetime(data['date'])

monthly_average = data.resample('M', on='date').mean()

monthly_average['date'] = monthly_average.index.strftime('%Y-%m-15')

monthly_average.to_csv("AylikOrtalamalarSana.csv", index=False)