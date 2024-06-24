import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

df=pd.read_csv('C:/Users/Monster/Desktop/Introduction to Data Science Project/countries.csv')
df = df[(df['Country'] == 'Kyrgyzstan') & (df['commodity'] == 'Tomatoes')]
df['precipitation'].fillna(df['precipitation'].mean(), inplace=True)
df['windStrength'].fillna(df['windStrength'].mean(), inplace=True)
df['pressure'].fillna(df['pressure'].mean(), inplace=True)
df['averageTemperature'].fillna(df['averageTemperature'].mean(), inplace=True)


df['usdprice'].fillna(df['usdprice'].mean(), inplace=True)
df1=df.copy()

df1=df1.dropna()

multidata=df.copy()

X = multidata[['averageTemperature', 'windStrength']]
y = multidata['usdprice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_model = SVR()
svm_model.fit(X_train_scaled, y_train)

y_head_svm = svm_model.predict(X_test_scaled)

r2_svm = r2_score(y_test, y_head_svm)
print('SVM r2 score =', r2_svm)

plt.plot(y_test.values, color='r', label='Actual')
plt.plot(y_head_svm, color='green', label='SVM Predicted')
plt.legend()
plt.show()

rmse_svm = np.sqrt(mean_squared_error(y_test, y_head_svm))
print('SVM Root Mean Squared Error (RMSE) =', rmse_svm)