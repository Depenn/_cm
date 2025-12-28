import cmath
import math

# 1. Implement the Forward Transform
def dft(x):
    N = len(x)
    X = [] # This will hold the complex frequency results
    
    # Outer loop: for each frequency bin k
    for k in range(N):
        sum_val = 0
        # Inner loop: sum over all time samples n
        for n in range(N):
            # FORMULA: x[n] * e^(-j * 2*pi * k * n / N)
            # Exponent logic: -2j * pi * k * n / N
            phi = -2j * cmath.pi * k * n / N
            sum_val += x[n] * cmath.exp(phi)
            
        X.append(sum_val)
    return X

# 2. Implement the Inverse Transform
def idft(X):
    N = len(X)
    x_recon = []
    
    # Outer loop: for each time sample n
    for n in range(N):
        sum_val = 0
        # Inner loop: sum over all frequency bins k
        for k in range(N):
            # FORMULA: X[k] * e^(j * 2*pi * k * n / N)
            # Notice the positive sign for IDFT
            phi = 2j * cmath.pi * k * n / N
            sum_val += X[k] * cmath.exp(phi)
            
        # And divide by N at the very end
        x_recon.append(sum_val / N)
        
    return x_recon

# 3. Test it
signal = [1, 0, 1, 0]
freq = dft(signal)
reconstructed = idft(freq)

print("Original:", signal)
print("Frequency Domain:", [complex(round(x.real, 2), round(x.imag, 2)) for x in freq])
print("Reconstructed:", [round(x.real) for x in reconstructed])
# We use .real because the output will technically be complex (e.g., 1+0j)
