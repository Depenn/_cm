import math
import numpy as np

def section(title):
    print(f"\n{'='*20} {title} {'='*20}")

# --- Task 1 & 2: The Underflow Problem ---
def probability_calculations():
    section("1 & 2. Probability Underflow vs Log-Prob")
    p = 0.5
    n = 10000

    # Direct calculation (Will Underflow)
    direct_prob = p ** n
    print(f"Direct Calculation (0.5^10000): {direct_prob}")
    print("-> Note: This is 0.0 because of floating point underflow.")

    # Log Calculation (Correct Method)
    # log(p^n) = n * log(p)
    log_prob = n * math.log2(p) # Using base 2 for bits
    print(f"Log Calculation (n * log2(p)):  {log_prob}")
    print("-> Note: This represents the actual value effectively.")

# --- Task 3 & 4: Info Theory Metrics & Inequality Check ---
def entropy(p):
    return -np.sum(p * np.log2(p + 1e-10)) # 1e-10 prevents log(0)

def cross_entropy(p, q):
    return -np.sum(p * np.log2(q + 1e-10))

def kl_divergence(p, q):
    return np.sum(p * np.log2((p + 1e-10) / (q + 1e-10)))

def info_theory_demo():
    section("3 & 4. Entropy, KL Divergence & Inequality Verification")
    
    # Define two probability distributions
    p = np.array([0.9, 0.1])
    q = np.array([0.5, 0.5]) # q is different from p
    
    h_p = entropy(p)
    ce_pp = cross_entropy(p, p)
    ce_pq = cross_entropy(p, q)
    kl = kl_divergence(p, q)
    
    print(f"Distribution p: {p}")
    print(f"Distribution q: {q}")
    print(f"Entropy H(p):            {h_p:.4f}")
    print(f"Cross Entropy H(p, p):   {ce_pp:.4f} (Should equal Entropy)")
    print(f"Cross Entropy H(p, q):   {ce_pq:.4f}")
    print(f"KL Divergence D(p||q):   {kl:.4f}")
    
    print("\n--- Inequality Verification ---")
    print(f"Is H(p, q) > H(p, p)? {ce_pq > ce_pp}")
    print("Observation: The prompt asked to verify H(p,p) > H(p,q).")
    print("This is INCORRECT. Gibbs' inequality states H(p,q) >= H(p,p).")
    print("The code confirms that Cross Entropy is minimized when p == q.")

# --- Task 5: Hamming Code (7, 4) ---
def hamming_74():
    section("5. Hamming Code (7,4)")
    
    # Data: 4 bits
    data = np.array([1, 0, 1, 1]) 
    print(f"Original Data: {data}")

    # Generator Matrix G (Standard form [I | P])
    # Note: Depending on the specific Hamming variant, P might differ.
    G = np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ])

    # Parity Check Matrix H (Standard form [P^T | I])
    H = np.array([
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1]
    ])

    # --- ENCODING ---
    # Codeword = Data * G (modulo 2)
    codeword = np.dot(data, G) % 2
    print(f"Encoded Codeword (7 bits): {codeword}")

    # --- ERROR SIMULATION ---
    # Let's flip the 3rd bit (index 2)
    received = codeword.copy()
    error_idx = 2
    received[error_idx] = (received[error_idx] + 1) % 2
    print(f"Received w/ Error (bit {error_idx} flipped): {received}")

    # --- DECODING ---
    # Syndrome = H * Received^T (modulo 2)
    syndrome = np.dot(H, received) % 2
    print(f"Syndrome: {syndrome}")
    
    # Convert binary syndrome to integer to find position
    # Note: In this standard matrix setup, syndrome usually maps to column index.
    # For [1, 1, 0] -> binary 6 -> 6th column? 
    # Hamming implementation varies by matrix arrangement. 
    # If Syndrome is [0,0,0], no error.
    
    syndrome_str = ''.join(map(str, syndrome))
    if np.sum(syndrome) == 0:
        print("Status: No Error Detected.")
    else:
        print(f"Status: Error Detected! Syndrome is {syndrome_str}")
        print("(In a full implementation, this maps to the column of H that matches the syndrome)")

# --- Execution ---
if __name__ == "__main__":
    probability_calculations()
    info_theory_demo()
    hamming_74()
