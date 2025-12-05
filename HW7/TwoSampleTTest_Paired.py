import numpy as np
from scipy import stats

def manual_t_test_paired(before, after):
    """
    Scenario: Paired T-Test (Dependent)
    Assumption: Same subjects measured at two different times.
    Logic: This is a 1-sample T-test on the DIFFERENCE (D).
    """
    # Calculate differences (D = After - Before)
    differences = np.array(after) - np.array(before)
    
    # Mean of differences
    d_bar = np.mean(differences)
    
    # Standard deviation of differences (ddof=1)
    s_d = np.std(differences, ddof=1)
    n = len(differences)
    
    # Formula: t = (d_bar - 0) / (Sd / sqrt(n))
    # We compare against 0 because Null Hypothesis assumes NO change.
    t_stat = d_bar / (s_d / np.sqrt(n))
    
    # Degrees of freedom
    df = n - 1
    
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
    
    return t_stat, p_value

# --- Usage Example ---
if __name__ == "__main__":
    # Example: Weight before and after a diet program
    w_before = [80, 85, 78, 90, 95]
    w_after  = [78, 83, 77, 88, 92]
    
    t, p = manual_t_test_paired(w_before, w_after)
    
    print(f"--- Paired T-Test Results ---")
    print(f"Mean Difference: {np.mean(np.array(w_after) - np.array(w_before))}")
    print(f"T-Statistic: {t:.4f}")
    print(f"P-Value: {p:.4f}")
