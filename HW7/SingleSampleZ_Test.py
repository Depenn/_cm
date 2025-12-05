import numpy as np
from scipy import stats

def manual_z_test(data, pop_mean, pop_std):
    """
    Scenario: Single Sample Z-Test
    Assumption: Population standard deviation (sigma) is KNOWN.
    """
    n = len(data)
    sample_mean = np.mean(data)
    
    # Formula: Z = (X_bar - mu) / (sigma / sqrt(n))
    standard_error = pop_std / np.sqrt(n)
    z_score = (sample_mean - pop_mean) / standard_error
    
    # P-value (Two-tailed test)
    # We look up the cumulative density up to |z| and subtract from 1 to get the tail,
    # then multiply by 2 for both tails.
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    
    return z_score, p_value

# --- Usage Example ---
if __name__ == "__main__":
    # Example: IQ scores (mean=100, sigma=15)
    sample_data = [110, 105, 115, 120, 112, 108, 109, 118, 114, 111]
    
    z, p = manual_z_test(sample_data, pop_mean=100, pop_std=15)
    
    print(f"--- Z-Test Results ---")
    print(f"Sample Mean: {np.mean(sample_data)}")
    print(f"Z-Score: {z:.4f}")
    print(f"P-Value: {p:.4f}")
