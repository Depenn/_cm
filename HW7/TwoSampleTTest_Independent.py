import numpy as np
from scipy import stats

def manual_t_test_ind(group1, group2):
    """
    Scenario: Independent Two-Sample T-Test
    Assumption: Two separate groups, assuming equal variance (Pooled).
    """
    n1 = len(group1)
    n2 = len(group2)
    mean1 = np.mean(group1)
    mean2 = np.mean(group2)
    
    # Calculate Variances (ddof=1)
    var1 = np.var(group1, ddof=1)
    var2 = np.var(group2, ddof=1)
    
    # Calculate Pooled Variance (Sp^2)
    # Formula: ((n1-1)s1^2 + (n2-1)s2^2) / (n1+n2-2)
    numerator = (n1 - 1)*var1 + (n2 - 1)*var2
    denominator = n1 + n2 - 2
    pooled_var = numerator / denominator
    
    # Standard Error for difference of means
    se_diff = np.sqrt(pooled_var * (1/n1 + 1/n2))
    
    # t-statistic
    t_stat = (mean1 - mean2) / se_diff
    
    # Degrees of freedom
    df = n1 + n2 - 2
    
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
    
    return t_stat, p_value

# --- Usage Example ---
if __name__ == "__main__":
    # Example: Test scores from Class A vs Class B
    class_a = [85, 88, 90, 92, 86]
    class_b = [78, 82, 80, 85, 79]
    
    t, p = manual_t_test_ind(class_a, class_b)
    
    print(f"--- Independent T-Test Results ---")
    print(f"Mean A: {np.mean(class_a)}, Mean B: {np.mean(class_b)}")
    print(f"T-Statistic: {t:.4f}")
    print(f"P-Value: {p:.4f}")
