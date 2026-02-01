import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

# 1. Fetch Data
# We use 'GC=F' which is the Gold Futures ticker
df = yf.download('GC=F', start='2018-01-01', end='2026-02-01')

# 2. Basic Feature Engineering
# We create 'Moving Averages' to help the model see trends
df['S_3'] = df['Close'].rolling(window=3).mean()
df['S_9'] = df['Close'].rolling(window=9).mean()
df = df.dropna()

# Define Independent variables (X) and Dependent variable (y)
X = df[['S_3', 'S_9']]
y = df['Close']

# 3. Split Data
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 4. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Prediction & Accuracy
predicted_price = model.predict(X_test)

print(f"Model Accuracy (R2 Score): {model.score(X_test, y_test):.2f}")
print(f"Mean Absolute Error: ${metrics.mean_absolute_error(y_test, predicted_price):.2f}")

# 6. Visualization
plt.figure(figsize=(10,5))
plt.plot(y_test.values, color='blue', label='Actual Price')
plt.plot(predicted_price, color='red', label='Predicted Price')
plt.title('Gold Price Prediction (Linear Regression)')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
