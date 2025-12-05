# Information Theory

This repository contains the Python implementation for the Information Theory homework. It covers probability underflow issues, entropy metrics, inequality verifications, and Hamming Code implementation.

## 📌 Overview

The script `hw8.py` performs the following tasks:

1.  **Probability Underflow Demonstration:** Shows how calculating $0.5^{10000}$ directly results in `0.0` due to floating-point limitations.
2.  **Log-Probability Calculation:** Solves the underflow issue using $\log(p^n) = n \log p$.
3.  **Metrics Implementation:** Calculates Entropy $H(p)$, Cross-Entropy $H(p,q)$, and KL Divergence $D_{KL}(p||q)$.
4.  **Inequality Verification (Correction):** Verifies the relationship between Self-Entropy and Cross-Entropy.
5.  **Hamming Code (7,4):** Implements encoding, error simulation, and syndrome decoding using Matrix operations.

## ⚠️ Important Note on Gibbs' Inequality

The assignment prompt requested a verification that `cross_entropy(p,p) > cross_entropy(p,q)`.

**This premise is mathematically incorrect.**

According to **Gibbs' Inequality**, Cross-Entropy is minimized when the probability distribution $q$ matches $p$. Therefore, assuming $p \neq q$:
$$H(p,q) > H(p,p)$$

My code demonstrates this correct relationship, proving that the prompt contained a typo.

## 📚 Theory Explanation (Theoretical Concepts)

### 1. 夏農信道編碼定理 (Shannon's Channel Coding Theorem)
該定理指出，對於任何給定的通信信道，都存在一個最大傳輸速率，稱為**信道容量 (Channel Capacity, C)**。
* 只要訊息傳輸速率 $R < C$，理論上就存在一種編碼方式，可以使誤碼率 (Error Probability) 任意接近於零。
* 這打破了以往認為「要減少錯誤必須降低傳輸速度」的觀念。

### 2. 夏農-哈特利定理 (Shannon-Hartley Theorem)
該定理量化了在高斯白噪聲干擾下的信道容量。公式如下：
$$C = B \cdot \log_2(1 + \frac{S}{N})$$
* $C$: 信道容量 (bit/s)
* $B$: 頻寬 (Hz)
* $S/N$: 信噪比 (Signal-to-Noise Ratio)

此定理說明了若要提升傳輸速度，必須擴大頻寬 ($B$) 或增強信號品質 ($S/N$)。

## 🛠️ Requirements & Usage

### Dependencies
* Python 3.x
* Numpy

```bash
pip install numpy
