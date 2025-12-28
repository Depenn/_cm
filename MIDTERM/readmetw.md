# 期中作業：比特幣價格預測之蒙地卡羅模擬 (Monte Carlo Simulation)

**姓名：** 林順義 (Lin Shun-Yi)
**學號：** 111310521
**系級：** 資工二
**課程：** 數學與程式設計

---

## 1. 專案描述 (Project Description)
本程式執行數學模擬，旨在預測未來 30 天的比特幣 (BTC-USD) 價格走勢。本專案採用基於 **幾何布朗運動 (Geometric Brownian Motion, GBM)** 模型的 **蒙地卡羅模擬 (Monte Carlo Simulation)** 方法。

本專案的目標並非絕對精準地預測未來價格，而是進行 **風險評估 (Risk Assessment)**，並根據過去一年的歷史數據，計算價格觸及特定目標的機率。

### 主要功能
* **即時數據：** 使用 `yfinance` 抓取即時市場數據。
* **隨機建模：** 模擬 1,000 種不同的未來價格路徑。
* **風險分析：** 計算風險值 (Value at Risk, VaR) 以及達到特定價格目標（例如 10 萬美元）的機率。

## 2. 數學基礎 (Mathematical Foundation)
本程式的核心基於被稱為 **幾何布朗運動 (Geometric Brownian Motion)** 的隨機微分方程 (SDE)：

$$S_t = S_{t-1} \cdot e^{(\mu - \frac{\sigma^2}{2})\Delta t + \sigma \epsilon \sqrt{\Delta t}}$$

其中：
* **$S_t$**：時間 $t$ 的預測價格。
* **$S_{t-1}$**：前一個時間步的價格。
* **$\mu$ (漂移率/Drift)**：預期每日回報，根據歷史的 *對數收益率 (Logarithmic Returns)* 計算得出。
* **$\sigma$ (波動率/Volatility)**：收益率的標準差，代表市場風險。
* **$\epsilon$ (隨機擾動/Random Shock)**：來自標準常態分佈 $N(0,1)$ 的隨機變數。

### 為什麼使用對數收益率？
我使用了 *對數收益率* $\ln(\frac{P_t}{P_{t-1}})$ 而非 *簡單收益率*。這是因為在資產價格模型中，通常假設價格服從對數常態分佈 (Log-Normal distribution)，這在數學上對於長期時間序列建模更為精確，且能確保價格恆為非負值。

## 3. 實作細節 (Implementation Details)
本專案使用 **Python** 實作，並使用了以下函式庫：

* **`yfinance`**：用於檢索歷史市場數據。
* **`numpy`**：用於高效能向量運算和矩陣計算（有效處理 1,000 種情境）。
* **`scipy.stats`**：具體使用了 `norm.ppf` (百分位點函數)，用於生成常態分佈的隨機變數。
* **`matplotlib`**：用於視覺化模擬路徑和最終機率分佈。

## 4. 分析結果 (Analysis Results)
基於對未來 30 天（2025 年 12 月預測）的 1,000 次模擬情境：

* **起始價格：** 約 $90,394
* **預期平均值 (Mean)：** 約 $89,676 (根據歷史漂移率，顯示輕微看跌/盤整趨勢)。
* **價格 > $100k 的機率：** **18%**
* **風險 (VaR 95%)：** 有 5% 的機率價格可能跌至 **$72,822** 或更低。

### 視覺化圖表
![Simulation Result](https://github.com/Depenn/_cm/blob/0d193f67c55f7f2926db1813a1a6ca39015da921/MIDTERM/Screenshot%202025-12-28%20235136.png)
*(圖表說明：左側顯示 1,000 條蒙地卡羅模擬路徑。右側顯示最終價格的分佈與風險閾值)*

## 5. 如何執行 (How to Run)
1.  安裝依賴套件：
    ```bash
    pip install yfinance numpy pandas matplotlib scipy
    ```
2.  執行腳本：
    ```bash
    python main.py
    ```

## 6. 參考資料 (References)
本專案的邏輯與實作基於：
* 幾何布朗運動的標準金融建模理論。
* Python 函式庫官方文件 (`numpy`, `pandas`, `yfinance`).
