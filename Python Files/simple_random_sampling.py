import pandas as pd
import numpy as np
from random import sample

file_path = r"C:\Users\yasin\Desktop\Ülkeler\countries.csv"
df = pd.read_csv(file_path)

selected_foods = df[(df['commodity'] == 'Tomatoes') & (df['Country'] == 'Kyrgyzstan')]

temperature_list=list(selected_foods['averageTemperature'])
sample_list=sample(temperature_list,120)

def mean_function_list(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    mean=sum/len(list)
    print(mean)
mean_function_list(sample_list)
