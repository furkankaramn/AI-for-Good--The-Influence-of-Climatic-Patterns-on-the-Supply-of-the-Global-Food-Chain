import pandas as pd
from scipy.stats import mannwhitneyu

csv_file_path = r"C:\Users\Monster\Downloads\countries.csv"

df = pd.read_csv(csv_file_path, parse_dates=['date'])
df['date'] = pd.to_datetime(df['date'], errors='coerce')

df = df.dropna(subset=['date', 'commodity', 'averageTemperature', 'usdprice'])

commodity1 = 'Tomatoes'
commodity2 = 'Potatoes'

group1_data_temp = df[df['commodity'] == commodity1]['averageTemperature']
group2_data_temp = df[df['commodity'] == commodity2]['averageTemperature']

group1_data_price = df[df['commodity'] == commodity1]['usdprice']
group2_data_price = df[df['commodity'] == commodity2]['usdprice']

if len(group1_data_temp) > 0 and len(group2_data_temp) > 0 and len(group1_data_price) > 0 and len(group2_data_price) > 0:
    
    stat_temp, p_value_temp = mannwhitneyu(group1_data_temp, group2_data_temp)
    print(f'Statistic for Temperature: {stat_temp}, p-value for Temperature: {p_value_temp}')

    stat_price, p_value_price = mannwhitneyu(group1_data_price, group2_data_price)
    print(f'Statistic for Price: {stat_price}, p-value for Price: {p_value_price}')

    if p_value_temp > 0.05:
        print(f'There is no median difference in temperature between the two groups (p-value: {p_value_temp}).')
    else:
        print(f'There is a median difference in temperature between the two groups (p-value: {p_value_temp}).')

    if p_value_price > 0.05:
        print(f'There is no median difference in price between the two groups (p-value: {p_value_price}).')
    else:
        print(f'There is a median difference in price between the two groups (p-value: {p_value_price}).')
else:
    print('Both groups must contain data.')

