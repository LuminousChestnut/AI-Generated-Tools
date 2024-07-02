import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取金融时间序列数据
data = pd.read_csv('financial_data.csv')  # 假设数据存储在financial_data.csv文件中
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# RSI（相对强弱指数）
def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# KDJ指标
def calculate_kdj(data, n=9, m1=3, m2=3):
    low_n = data['Low'].rolling(window=n).min()
    high_n = data['High'].rolling(window=n).max()
    rsv = (data['Close'] - low_n) / (high_n - low_n) * 100
    k = rsv.ewm(span=m1).mean()
    d = k.ewm(span=m2).mean()
    j = 3 * k - 2 * d
    return k, d, j

# MACD（平滑异同平均线）
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    macd_hist = macd - signal
    return macd, signal, macd_hist

# BOLL（布林带）
def calculate_bollinger_bands(data, window=20):
    sma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    upper_band = sma + (2 * std)
    lower_band = sma - (2 * std)
    return sma, upper_band, lower_band

# OBV（能量潮指标）
def calculate_obv(data):
    obv = np.where(data['Close'] > data['Close'].shift(1), data['Volume'], 
                   np.where(data['Close'] < data['Close'].shift(1), -data['Volume'], 0))
    obv = np.cumsum(obv)
    return obv

# 计算各技术指标
data['RSI'] = calculate_rsi(data)
data['K'], data['D'], data['J'] = calculate_kdj(data)
data['MACD'], data['MACD_Signal'], data['MACD_Hist'] = calculate_macd(data)
data['SMA'], data['Upper_Band'], data['Lower_Band'] = calculate_bollinger_bands(data)
data['OBV'] = calculate_obv(data)

# 可视化技术指标
plt.figure(figsize=(14, 10))

# 收盘价及布林带
plt.subplot(3, 1, 1)
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA'], label='SMA', linestyle='--')
plt.plot(data['Upper_Band'], label='Upper Band', linestyle='--')
plt.plot(data['Lower_Band'], label='Lower Band', linestyle='--')
plt.title('Bollinger Bands')
plt.legend()

# MACD
plt.subplot(3, 1, 2)
plt.plot(data['MACD'], label='MACD')
plt.plot(data['MACD_Signal'], label='MACD Signal', linestyle='--')
plt.bar(data.index, data['MACD_Hist'], label='MACD Hist', color='gray', alpha=0.5)
plt.title('MACD')
plt.legend()

# RSI及OBV
plt.subplot(3, 1, 3)
plt.plot(data['RSI'], label='RSI')
plt.plot(data['OBV'], label='OBV')
plt.title('RSI & OBV')
plt.legend()

plt.tight_layout()
plt.show()
