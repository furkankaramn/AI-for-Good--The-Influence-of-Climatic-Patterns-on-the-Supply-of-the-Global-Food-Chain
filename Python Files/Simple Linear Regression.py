import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn import metrics


df = pd.read_csv('C:/Users/Monster/Desktop/Introduction to Data Science Project/countries.csv')


df['averageTemperature'].fillna(df['averageTemperature'].mean(), inplace=True)


df['usdprice'].fillna(df['usdprice'].mean(), inplace=True)


filtered_df = df[(df['Country'] == 'Kyrgyzstan') & (df['commodity'] == 'Tomatoes')]


X = filtered_df[['averageTemperature']]

y = filtered_df['usdprice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


regressor = LinearRegression()
regressor.fit(X_train, y_train)


y_pred = regressor.predict(X_test)

df_result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df_result)

df_result.head(10).plot(kind='bar', figsize=(16, 10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
plt.grid(which='minor', linestyle='-', linewidth='0.5', color='black')
plt.show()



print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
