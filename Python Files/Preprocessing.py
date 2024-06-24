import pandas as pd

df = pd.read_csv('C:/Users/Monster/Desktop/Country/Yemen.csv')

df['usdprice'] = pd.to_numeric(df['usdprice'].replace('[^\d.]', '', regex=True), errors='coerce')

df = df.drop(columns=['admin1', 'admin2', 'market', 'latitude', 'longitude', 'unit', 'priceflag', 'pricetype', 'currency', 'price','category'])

start_date = '2021-01-15'
end_date = '2021-12-15'

df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)].copy()

df_filtered['date'] = pd.to_datetime(df_filtered['date'], errors='coerce')
df_filtered = df_filtered[df_filtered['date'].dt.day == 15]

print(df_filtered)

df_filtered.to_csv('C:/Users/Monster/Desktop/Country/Yemen_with_country_filtered.csv', index=False)
