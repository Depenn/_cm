import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    Solves a constant coefficient homogeneous ODE given its characteristic equation coefficients.
    Format: a_n y^(n) + ... + a_1 y' + a_0 y = 0
    """
    # 1. Find roots of the characteristic equation
    roots = np.roots(coefficients)
    
    # 2. Process roots to handle floating point inaccuracies
    # We round them to avoid treating 1.999999 as different from 2.0
    tol = 1e-5
    processed_roots = []
    
    for r in roots:
        real_part = np.round(r.real, 5)
        imag_part = np.round(r.imag, 5)
        
        # If imaginary part is very small, treat as 0 (Real root)
        if abs(imag_part) < tol:
            processed_roots.append(real_part + 0j)
        else:
            processed_roots.append(real_part + 1j * imag_part)

    # 3. Sort roots to ensure deterministic output order (Real first, then Imag)
    # We use a custom sort key
    processed_roots.sort(key=lambda x: (x.real, abs(x.imag), x.imag))

    # 4. Generate the solution string
    terms = []
    c_index = 1  # Counter for C_1, C_2...
    
    # Track multiplicity: how many times have we seen this root?
    # We need a way to track "usage" of a root value
    usage_counter = Counter()
    
    # We must skip the conjugate of a complex pair to avoid double counting terms
    # (e.g., 2j generates cos/sin, we don't need -2j to generate them again)
    skip_indices = set()

    for i, r in enumerate(processed_roots):
        if i in skip_indices:
            continue

        real = r.real
        imag = r.imag
        
        # Get current multiplicity count (k) for the extra 'x' term
        # If root is 2, 2, 2 -> k=0, then k=1, then k=2
        # We define a unique key for the counter
        root_key = (real, abs(imag)) 
        k = usage_counter[root_key]
        usage_counter[root_key] += 1
        
        # Format the 'x' multiplier: "x" or "x^2"
        if k == 0:
            x_term = ""
        elif k == 1:
            x_term = "x"
        else:
            x_term = f"x^{k}"

        # CASE A: Real Root
        if abs(imag) < tol:
            # Format: C_n * x^k * e^(rx)
            term = f"C_{c_index}{x_term}e^({real}x)"
            terms.append(term)
            c_index += 1
            
        # CASE B: Complex Root (alpha +/- beta i)
        else:
            # Only process positive imaginary part (or first of the pair)
            # Find its conjugate in the remaining list to mark as skipped
            for j in range(i + 1, len(processed_roots)):
                other = processed_roots[j]
                if np.isclose(other.real, real) and np.isclose(other.imag, -imag):
                    skip_indices.add(j)
                    break
            
            # Complex solution format: e^(ax) * (C_1 cos(bx) + C_2 sin(bx))
            # But the requirement asks for distributed format: C_1 e^(ax)cos(bx) + ...
            
            # Clean up 0.0 in exponent
            exp_part = f"e^({real}x)" if abs(real) > tol else ""
            
            # Cosine term
            term_cos = f"C_{c_index}{x_term}{exp_part}cos({abs(imag)}x)"
            c_index += 1
            terms.append(term_cos)
            
            # Sine term
            term_sin = f"C_{c_index}{x_term}{exp_part}sin({abs(imag)}x)"
            c_index += 1
            terms.append(term_sin)

    return "y(x) = " + " + ".join(terms)

# --- COPY THE TEST BLOCK BELOW FROM THE GITHUB PAGE TO VERIFY ---
print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))
