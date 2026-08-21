from sklearn import model_selection
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

np.random.seed(42)
#
ticker = "AAPL"  # Apple stock
# auto_adjust=True automatically adjusts prices and removes 'Adj Close'
data = yf.download(ticker, period="3y", interval="1d", progress=False, auto_adjust=True)

print(" Data Loaded Successfully!\n")
print(data.head())

print("\n DESCRIPTIVE STATISTICS")
print(data.describe())

# Calculate daily returns
data['Returns'] = data['Close'].pct_change()

plt.figure(figsize=(6,4))
plt.plot(data['Returns'])
plt.title("Daily Returns Over Time")
plt.xlabel("Date")
plt.ylabel("Returns")
plt.show()

Mean = data['Close'].mean()
print(f"\nMean Close Price: {Mean.item():.2f}")

Std=data['Close'].std()
print(f"Standard Deviation of Close Price: {Std.item():.2f}")

print("\n Correlation  Matrix ")
corr_matrix=data.corr()
print(corr_matrix)

sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

data.dropna(inplace=True)

data['Volatility']=data['High']-data['Low']


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

X=data[['Volume','Close','Volatility']]
y=data['Returns']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("R² Score:",r2_score(y_test,y_pred))

plt.scatter(y_test,y_pred)
plt.xlabel("Actual Retirns")
plt.ylabel("Predicted Returns")
plt.title("Actual vs. Predicted Returns")

plt.show()