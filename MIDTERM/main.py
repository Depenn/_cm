import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- KONFIGURASI USER ---
TICKER = "BTC-USD"
START_DATE = "2024-12-01"
END_DATE = "2025-12-01" 
SIMULATION_DAYS = 30    # Prediksi 30 hari
N_SIMULATIONS = 1000    # 1000 Skenario
TARGET_PRICE = 100000   # Kita mau hitung peluang tembus angka ini

def get_data(ticker, start, end):
    print(f"[PROCESS] Mengambil data {ticker}...")
    data = yf.download(ticker, start=start, end=end, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    
    if 'Adj Close' in data.columns:
        df = data[['Adj Close']].copy()
    elif 'Close' in data.columns:
        df = data[['Close']].copy()
    else:
        raise ValueError("Kolom harga tidak ditemukan.")
    
    df.columns = ['Price']
    return df

def calculate_log_returns(df):
    df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1))
    df.dropna(inplace=True)
    return df

def monte_carlo_simulation(df, days, iterations):
    # Parameter Statistik
    u = df['Log_Returns'].mean()
    var = df['Log_Returns'].var()
    drift = u - (0.5 * var)
    sigma = df['Log_Returns'].std()
    
    last_price = df['Price'].iloc[-1]
    
    # Random Generator (Geometric Brownian Motion)
    daily_returns = np.exp(drift + sigma * norm.ppf(np.random.rand(days, iterations)))
    
    price_paths = np.zeros((days + 1, iterations))
    price_paths[0] = last_price
    
    for t in range(1, days + 1):
        price_paths[t] = price_paths[t-1] * daily_returns[t-1]
        
    return price_paths

if __name__ == "__main__":
    try:
        # 1. PREP
        df_bitcoin = get_data(TICKER, START_DATE, END_DATE)
        df_bitcoin = calculate_log_returns(df_bitcoin)
        last_price = df_bitcoin['Price'].iloc[-1]

        # 2. SIMULASI
        price_paths = monte_carlo_simulation(df_bitcoin, SIMULATION_DAYS, N_SIMULATIONS)
        final_prices = price_paths[-1] # Harga di hari ke-30 dari semua 1000 skenario

        # 3. ANALISIS PROBABILITAS (MATH PART)
        # Hitung berapa skenario yang harganya > TARGET_PRICE
        over_target = np.sum(final_prices > TARGET_PRICE)
        prob_success = (over_target / N_SIMULATIONS) * 100

        # Hitung Value at Risk (VaR) 95%
        # Artinya: Kita 95% yakin harga tidak akan jatuh di bawah angka ini
        var_95 = np.percentile(final_prices, 5)

        print(f"\n--- ANALISIS RISIKO (Based on {N_SIMULATIONS} scenarios) ---")
        print(f"Harga Sekarang         : ${last_price:,.2f}")
        print(f"Peluang Tembus ${TARGET_PRICE/1000:.0f}k  : {prob_success:.2f}%")
        print(f"VaR (Risk Bottom 5%)   : ${var_95:,.2f}")
        print(f"Rata-rata Ekspektasi   : ${np.mean(final_prices):,.2f}")

        # 4. VISUALISASI DUAL PANEL
        print("[PROCESS] Membuat Visualisasi Lengkap...")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # PANEL KIRI: Spaghetti Plot
        ax1.plot(price_paths, color='cyan', alpha=0.1, linewidth=0.5)
        ax1.plot(np.mean(price_paths, axis=1), color='red', linewidth=2, label='Mean Path')
        ax1.axhline(y=last_price, color='black', linestyle='--', label='Start Price')
        ax1.set_title(f'Monte Carlo Simulation: {TICKER} (30 Days)')
        ax1.set_xlabel('Day')
        ax1.set_ylabel('Price (USD)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # PANEL KANAN: Histogram Distribusi Akhir
        ax2.hist(final_prices, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
        
        # Garis Target (Merah Putus-putus)
        ax2.axvline(x=TARGET_PRICE, color='red', linestyle='--', linewidth=2, label=f'Target ${TARGET_PRICE/1000:.0f}k')
        
        # Garis VaR (Hitam Putus-putus)
        ax2.axvline(x=var_95, color='orange', linestyle='--', linewidth=2, label=f'Risk 5% (${var_95/1000:.0f}k)')
        
        ax2.set_title(f'Distribution of Final Prices (Day 30)\nProb > ${TARGET_PRICE/1000:.0f}k: {prob_success:.2f}%')
        ax2.set_xlabel('Price (USD)')
        ax2.set_ylabel('Frequency')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        print("[SUCCESS] Project Selesai secara Teknis.")

    except Exception as e:
        print("\n[ERROR]", e)
