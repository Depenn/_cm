# HW7: Mathematical Principles of Hypothesis Testing

This repository contains the manual Python implementation of Z-tests and T-tests. 
Unlike standard implementations that rely on `scipy.stats` functions (black box), these scripts **manually calculate** the statistical formulas to demonstrate an understanding of the underlying mathematical derivations.

## 📂 Project Structure

| File Name | Description |
|-----------|-------------|
| `z_test_manual.py` | Z-Test (Single Sample) where population $\sigma$ is known. |
| `t_test_1samp_manual.py` | T-Test (Single Sample) where population $\sigma$ is unknown. |
| `t_test_ind_manual.py` | Independent Two-Sample T-Test (Pooled Variance). |
| `t_test_paired_manual.py` | Paired T-Test (Dependent Samples). |

---

## 🧮 Mathematical Derivations Implemented

The following formulas are explicitly programmed into the Python scripts:

### 1. Z-Test (Single Sample)
Used when the population standard deviation ($\sigma$) is **known**. According to the Central Limit Theorem, the sampling distribution of the mean is Normal.

$$Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$$

* **Implementation Detail:** We calculate the Standard Error using the known population $\sigma$.

### 2. T-Test (Single Sample)
Used when $\sigma$ is **unknown**. We estimate it using the sample standard deviation ($S$). This introduces uncertainty, requiring the T-distribution (Student's t).

$$t = \frac{\bar{X} - \mu_0}{S / \sqrt{n}}$$

* **Implementation Detail:** We use `ddof=1` when calculating standard deviation to ensure an unbiased estimator ($n-1$).

### 3. Independent Two-Sample T-Test
Used to compare means of two independent groups. This implementation assumes equal variance and uses the **Pooled Variance** ($S_p^2$) method.

**Pooled Variance Formula:**
$$S_p^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}$$

**T-Statistic Formula:**
$$t = \frac{(\bar{X}_1 - \bar{X}_2)}{S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

### 4. Paired T-Test (Dependent)
Used when samples are related (e.g., Pre-test vs Post-test). We reduce this to a single-sample test on the **differences** ($D$).

$$t = \frac{\bar{D} - 0}{S_d / \sqrt{n}}$$

* **Implementation Detail:** The script first calculates the difference vector $D = X_{after} - X_{before}$, then performs a standard T-test on $D$.

---

## 🚀 How to Run

Ensure you have `numpy` and `scipy` installed:

```bash
pip install numpy scipy
