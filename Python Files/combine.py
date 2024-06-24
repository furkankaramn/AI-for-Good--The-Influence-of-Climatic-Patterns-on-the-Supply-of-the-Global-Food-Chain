import pandas as pd

df1 = pd.read_csv("C:/Users/yasin/Desktop/ülkeler ürün fiyatları 2021/Turkiye_with_country_filtered.csv")

df2 = pd.read_csv("C:/Users/yasin/Desktop/sıcaklık/AylikOrtalamalar.csv")
df2 = df2.drop(columns=['tmin', 'tmax', 'snow', 'wdir', 'wpgt', 'tsun'])

df1['date'] = pd.to_datetime(df1['date'])
df2['date'] = pd.to_datetime(df2['date'])

df2 = df2.rename(columns={'tavg': 'averageTemperature', 'prcp': 'precipitation', 'wspd': 'windStrength', 'pres': 'pressure'})

merged_df = pd.merge(df1, df2, on='date')
merged_df['Country']='Turkiye'

print(merged_df.columns)

print(merged_df)

merged_df.to_csv("C:/Users/yasin/Desktop/merged_output6.csv", index=False)
