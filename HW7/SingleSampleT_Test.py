import numpy as np
from scipy import stats

def manual_t_test_1samp(data, pop_mean):
    """
    Scenario: Single Sample T-Test
    Assumption: Population std dev is UNKNOWN. Use Sample std dev.
    """
    n = len(data)
    sample_mean = np.mean(data)
    
    # Calculate Sample Standard Deviation
    # ddof=1 is crucial here to make it an "unbiased estimator" (dividing by n-1)
    sample_std = np.std(data, ddof=1)
    
    # Formula: t = (X_bar - mu) / (S / sqrt(n))
    standard_error = sample_std / np.sqrt(n)
    t_stat = (sample_mean - pop_mean) / standard_error
    
    # Degrees of freedom = n - 1
    df = n - 1
    
    # P-value (Two-tailed) using the T-distribution
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
    
    return t_stat, p_value

# --- Usage Example ---
if __name__ == "__main__":
    # Example: Factory parts target weight = 50g
    sample_weights = [48.5, 49.2, 50.1, 49.8, 49.0]
    
    t, p = manual_t_test_1samp(sample_weights, pop_mean=50)
    
    print(f"--- One-Sample T-Test Results ---")
    print(f"Sample Mean: {np.mean(sample_weights)}")
    print(f"T-Statistic: {t:.4f}")
    print(f"P-Value: {p:.4f}")
