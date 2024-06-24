import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

cal_housing = fetch_california_housing()
df = pd.read_csv('C:/Users/Monster/Desktop/Introduction to Data Science Project/countries.csv')

# Assuming 'averageTemperature' is one of the columns in your CSV file
# You can adjust this based on your actual column names
df = df[(df['commodity'] == 'Eggs')]

df['precipitation'].fillna(df['precipitation'].mean(), inplace=True)
df['windStrength'].fillna(df['windStrength'].mean(), inplace=True)
df['pressure'].fillna(df['pressure'].mean(), inplace=True)
df['averageTemperature'].fillna(df['averageTemperature'].mean(), inplace=True)

# Assuming 'usdprice' is one of the columns in your CSV file
# You can adjust this based on your actual column names
df['usdprice'] = df['usdprice'].fillna(df['usdprice'].mean())

X = df[['averageTemperature']]
y = df[['usdprice']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

degrees = np.arange(1, 16)
mse_values = []
r2_values = []

plt.figure(figsize=(15, 15))
for i, degree in enumerate(degrees, start=1):
    plt.subplot(5, 3, i)
    plt.tight_layout()

    poly = PolynomialFeatures(degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    y_pred = model.predict(X_test_poly)

    mse = mean_squared_error(y_test, y_pred)
    mse_values.append(mse)

    r2 = r2_score(y_test, y_pred)
    r2_values.append(r2)

    plt.tight_layout()
    plt.scatter(X_test, y_test, label='Real Values', color='black', alpha=0.5)

    x_range = np.linspace(X_test.min(), X_test.max(), 100)
    x_range_poly = poly.transform(x_range)
    y_pred_range = model.predict(x_range_poly)
    plt.plot(x_range, y_pred_range, label=f'Degree {degree}, MSE: {mse:.2f}, R^2: {r2:.2f}', linewidth=2)
    plt.title(f'Polynomial Regression: Degree {degree}')
    plt.xlabel('averageTemperature')
    plt.ylabel('usdprice')
    plt.legend()

plt.show()
