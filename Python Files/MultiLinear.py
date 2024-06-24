import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv('C:/Users/Monster/Desktop/Introduction to Data Science Project/countries.csv')
df = df[(df['commodity'] == 'Sugar')]

df['precipitation'].fillna(df['precipitation'].mean(), inplace=True)
df['windStrength'].fillna(df['windStrength'].mean(), inplace=True)
df['pressure'].fillna(df['pressure'].mean(), inplace=True)
df['averageTemperature'].fillna(df['averageTemperature'].mean(), inplace=True)
df['usdprice'].fillna(df['usdprice'].mean(), inplace=True)

df1 = df.copy()

df1 = df1.dropna()

multidata = df1.copy()

X = multidata[['averageTemperature', 'windStrength']]
Y = multidata['usdprice']

X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.3)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

vif_data = pd.DataFrame()
vif_data["column"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)

X_train_b = np.c_[np.ones((len(X_train_scaled), 1)), X_train_scaled]
X_val_b = np.c_[np.ones((len(X_val_scaled), 1)), X_val_scaled]
X_test_b = np.c_[np.ones((len(X_test_scaled), 1)), X_test_scaled]

ridge = Ridge(alpha=1.0)
model = ridge.fit(X_train_b, Y_train)

print("Coefficients (Theta):")
print(model.coef_)

Y_val_pred = model.predict(X_val_b)

mse_val = mean_squared_error(Y_val, Y_val_pred)
print("Mean Squared Error on Validation Set:", mse_val)

Y_test_pred = model.predict(X_test_b)

mse_test = mean_squared_error(Y_test, Y_test_pred)
print("Mean Squared Error on Test Set:", mse_test)

plt.scatter(Y_test, Y_test_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values on Test Set")
plt.show()


plt.scatter(Y_test, Y_test_pred, label='Actual vs Predicted')
plt.plot([min(Y_test), max(Y_test)], [min(Y_test), max(Y_test)], '--k', label='Perfectly Predicted')
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values on Test Set")
plt.legend()
plt.show()
