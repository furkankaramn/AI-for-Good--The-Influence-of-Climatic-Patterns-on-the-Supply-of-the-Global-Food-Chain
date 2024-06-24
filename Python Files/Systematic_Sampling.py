import pandas as pd
import numpy as np

file_path = r"C:\Users\yasin\Desktop\Ülkeler\countries.csv"
df = pd.read_csv(file_path)

selected_foods = df[(df['commodity'] == 'Tomatoes') & (df['Country'] == 'Kyrgyzstan')]

def systematic_sampling(selected_foods,step):
    indexes=np.arange(0,len(selected_foods),step=step)
    systematic_sample=selected_foods.iloc[indexes]
    return(systematic_sample)

systematic_sample=systematic_sampling(selected_foods,5)

print(systematic_sample['usdprice'].mean())
print(systematic_sample['averageTemperature'].mean())
