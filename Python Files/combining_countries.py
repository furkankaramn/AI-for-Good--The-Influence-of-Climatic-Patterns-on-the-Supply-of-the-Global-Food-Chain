import pandas as pd

csv_files = [
    r"C:\Users\yasin\Desktop\Ülkeler\Algeria.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Colombia.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\DemocraticRepublicOfCongo.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Egypt.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\India.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Indonesia.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Kyrgyzstan.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Peru.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Tajikistan.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Türkiye.csv",
    r"C:\Users\yasin\Desktop\Ülkeler\Yemen.csv"
]

dfs = [pd.read_csv(file) for file in csv_files]
merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_csv(r"C:\Users\yasin\Desktop\Ülkeler\countries.csv", index=False)
