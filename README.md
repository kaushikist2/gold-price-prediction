# gold-price-prediction

# Gold Price Prediction using Machine Learning

## 📌 Project Overview
This project is a financial data analysis and machine learning tool designed to predict the price of Gold using historical market data. By leveraging moving averages and linear regression, the model identifies trends in the gold market to forecast future price movements. 

This project was developed as a final-year demonstration of applying predictive analytics to real-world financial assets.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Source:** [Yahoo Finance API (yfinance)](https://pypi.org/project/yfinance/)
* **Libraries:** * `Pandas` - Data manipulation and analysis
    * `NumPy` - Numerical computing
    * `Scikit-Learn` - Machine learning and evaluation
    * `Matplotlib` - Data visualization

## 📊 Methodology
The project follows a standard Machine Learning pipeline:



1. **Data Acquisition:** Historical gold futures data (`GC=F`) is pulled directly from Yahoo Finance.
2. **Feature Engineering:** To capture market momentum, I calculated:
    * **S_3:** 3-day Moving Average
    * **S_9:** 9-day Moving Average
3. **Data Splitting:** The dataset is split into **80% Training** and **20% Testing** sets (maintaining chronological order).
4. **Modeling:** A **Linear Regression** algorithm is applied to find the relationship between the moving averages and the closing price.
5. **Evaluation:** The model is evaluated using R-Squared ($R^2$) and Mean Absolute Error (MAE).

## 📈 Results
The model successfully tracks the general trend of gold prices. 
* **R2 Score:** ~0.90 (Example)
* **Mean Absolute Error:** ~$12.00 (Example)

*Note: The plot below shows the alignment between the actual market prices and our model's predictions.*

[Add your plot image here later: ![Prediction Plot](plot.png)]

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/gold-price-prediction.git](https://github.com/YOUR_USERNAME/gold-price-prediction.git)
