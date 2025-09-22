import numpy as np

def root(c):
  while len(c) > 1 and abs(c[-1]) < 1e-14:
    c.pop()
    
  n = len(c) - 1;
  
  if n == 0:
    return "no roots"
  if n == 1:
    return [-c[0]/c[1]]
  
  
  companion = np.zeros((n, n))
  companion[1:, :-1] = np.eye(n-1)
  companion[0, :] = -np.array(c[:-1])
  
  roots = np.linalg.eigvals(companion)
  return roots
  
coeffs = [-8, 14, -7, 1]
print(root(coeffs))