# Midterm Assignment: Monte Carlo Simulation for Bitcoin Price Prediction

**Name:** 林順義 (Lin Shun-Yi)
**Student ID:** 111310521
**Department:** 資工二
**Course:** Mathematics and Coding

---

## 1. Project Description
This program performs a mathematical simulation to project Bitcoin (BTC-USD) price movements for the next 30 days. It utilizes the **Monte Carlo Simulation** method based on the **Geometric Brownian Motion (GBM)** model.

The objective is not to predict the future with certainty, but to conduct a **Risk Assessment** and calculate the probability of price targets based on historical data from the past year.

### Key Features
* **Real-time Data:** Fetches live market data using `yfinance`.
* **Stochastic Modeling:** Simulates 1,000 different future price paths.
* **Risk Analysis:** Calculates Value at Risk (VaR) and probability of hitting specific price targets (e.g., $100k).

## 2. Mathematical Foundation
The core of this program relies on the Stochastic Differential Equation (SDE) known as **Geometric Brownian Motion**:

$$S_t = S_{t-1} \cdot e^{(\mu - \frac{\sigma^2}{2})\Delta t + \sigma \epsilon \sqrt{\Delta t}}$$

Where:
* **$S_t$**: Projected price at time $t$.
* **$S_{t-1}$**: Price at the previous time step.
* **$\mu$ (Drift)**: Expected daily return, calculated from historical *Logarithmic Returns*.
* **$\sigma$ (Volatility)**: Standard deviation of returns, representing market risk.
* **$\epsilon$ (Random Shock)**: Random variable from the Standard Normal Distribution $N(0,1)$.

### Why Logarithmic Returns?
I utilized *Logarithmic Returns* $\ln(\frac{P_t}{P_{t-1}})$ instead of *Simple Returns*. This is because asset prices are assumed to follow a Log-Normal distribution, which is mathematically more accurate for long-term Time Series modeling and ensures prices remain non-negative.

## 3. Implementation Details
The project is implemented in **Python** using the following libraries:

* **`yfinance`**: For retrieving historical market data.
* **`numpy`**: For high-performance vector operations and matrix calculations (handling 1,000 scenarios efficiently).
* **`scipy.stats`**: specifically `norm.ppf` (Percent Point Function) to generate the random variables for the normal distribution.
* **`matplotlib`**: For visualizing the simulation paths and the final probability distribution.

## 4. Analysis Results
Based on 1,000 simulated scenarios for the next 30 days (December 2025 projection based on historical data):

* **Start Price:** ~$90,394
* **Expected Mean:** ~$89,676 (Indicates a slight bearish/sideways trend based on historical drift).
* **Probability > $100k:** **17.20%**
* **Risk (VaR 95%):** There is a 5% chance the price could drop to **$72,822** or lower.

### Visualization
![Simulation Result](https://github.com/Depenn/_cm/blob/0d193f67c55f7f2926db1813a1a6ca39015da921/MIDTERM/Screenshot%202025-12-28%20235136.png
)
*(Figure: Left panel shows 1,000 Monte Carlo simulation paths. Right panel shows the distribution of final prices with risk thresholds)*

## 5. How to Run
1.  Install dependencies:
    ```bash
    pip install yfinance numpy pandas matplotlib scipy
    ```
2.  Run the script:
    ```bash
    python main.py
    ```

## 6. References
The logic and implementation are based on:
* Standard financial modeling of Geometric Brownian Motion.
* Python library documentation (`numpy`, `pandas`, `yfinance`).
