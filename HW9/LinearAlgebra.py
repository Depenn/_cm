import numpy as np
import scipy.linalg

def section(title):
    print(f"\n{'='*20} {title} {'='*20}")

# --- 1. Recursive Determinant (The "Slow" Way) ---
def determinant_recursive(A):
    """
    Calculates determinant using Laplace expansion (O(n!)).
    Only for small matrices!
    """
    n = len(A)
    if n == 1:
        return A[0,0]
    if n == 2:
        return A[0,0]*A[1,1] - A[0,1]*A[1,0]
    
    det = 0
    for c in range(n):
        # Create minor matrix by removing row 0 and column c
        minor = np.delete(np.delete(A, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * A[0, c] * determinant_recursive(minor)
    return det

# --- 2. LU Decomposition & Determinant ---
def lu_det_demo(A):
    section("2. LU Decomposition & Determinant")
    P, L, U = scipy.linalg.lu(A)
    
    # Det(A) = Det(P) * Det(L) * Det(U)
    # Det(P) is usually +/- 1 based on swaps. Det(L) is 1 (diagonal is 1s). 
    # Det(U) is product of diagonals.
    
    # Scipy's P is a permutation matrix. det(P) is (-1)^swaps.
    det_P = np.linalg.det(P) 
    det_U = np.prod(np.diag(U))
    det_calc = det_P * det_U
    
    print(f"Matrix A:\n{A}")
    print(f"Calculated via LU (prod(diag(U)) * det(P)): {det_calc:.4f}")
    print(f"Numpy Reference det(A): {np.linalg.det(A):.4f}")

# --- 3. Decomposition Verification ---
def verify_decompositions(A):
    section("3. Verify LU, QR, SVD, Eigen")
    
    # LU
    P, L, U = scipy.linalg.lu(A)
    reconstructed_lu = P @ L @ U
    print(f"LU Error: {np.linalg.norm(A - reconstructed_lu):.4e}")

    # QR
    Q, R = np.linalg.qr(A)
    reconstructed_qr = Q @ R
    print(f"QR Error: {np.linalg.norm(A - reconstructed_qr):.4e}")

    # Eigen (Only for square)
    vals, vecs = np.linalg.eig(A)
    # A * v = lambda * v -> A = V * diag(vals) * inv(V)
    reconstructed_eig = vecs @ np.diag(vals) @ np.linalg.inv(vecs)
    print(f"Eigen Error: {np.linalg.norm(A - reconstructed_eig):.4e}")

    # SVD
    U_svd, S, Vt = np.linalg.svd(A)
    # Reconstruct: U * Sigma * Vt
    Sigma = np.zeros_like(A, dtype=float)
    np.fill_diagonal(Sigma, S)
    reconstructed_svd = U_svd @ Sigma @ Vt
    print(f"SVD Error:   {np.linalg.norm(A - reconstructed_svd):.4e}")

# --- 4. SVD via Eigen Decomposition ---
def svd_via_eigen(A):
    section("4. SVD via Eigen Decomposition")
    # A = U S V^T
    # A^T A = V S^2 V^T  -> V are eigenvectors of A^T A
    # A A^T = U S^2 U^T  -> U are eigenvectors of A A^T
    
    ATA = A.T @ A
    AAT = A @ A.T
    
    # Get V (Eigenvectors of ATA)
    vals_v, V = np.linalg.eigh(ATA)
    
    # Get U (Eigenvectors of AAT)
    vals_u, U = np.linalg.eigh(AAT)
    
    # Sort eigenvalues descending (numpy eigh sorts ascending usually)
    idx_v = vals_v.argsort()[::-1]
    vals_v = vals_v[idx_v]
    V = V[:, idx_v]
    
    idx_u = vals_u.argsort()[::-1]
    U = U[:, idx_u]
    
    # Singular values are sqrt of eigenvalues
    # Clip negative values due to float errors
    singular_values = np.sqrt(np.maximum(vals_v, 0))
    
    print("Calculated Singular Values (via Eigen):")
    print(singular_values)
    print("Numpy SVD Reference Singular Values:")
    print(np.linalg.svd(A)[1])
    
    print("\nNote: Reconstructing U and V signs manually is complex due to sign ambiguity in Eigenvectors.")

# --- 5. PCA Implementation ---
def pca_demo():
    section("5. PCA Implementation")
    # Sample Data: 5 samples, 3 features
    data = np.array([
        [2.5, 2.4, 0.5],
        [0.5, 0.7, 0.1],
        [2.2, 2.9, 0.6],
        [1.9, 2.2, 0.3],
        [3.1, 3.0, 0.8]
    ])
    
    print("Original Data (First 2 rows):\n", data[:2])
    
    # 1. Center the data
    mean = np.mean(data, axis=0)
    centered_data = data - mean
    
    # 2. Covariance Matrix
    cov_matrix = np.cov(centered_data.T)
    
    # 3. Eigen Decomposition
    values, vectors = np.linalg.eigh(cov_matrix)
    
    # Sort descending
    idx = values.argsort()[::-1]
    values = values[idx]
    vectors = vectors[:, idx]
    
    # 4. Project to top 2 Principal Components
    pc_vectors = vectors[:, :2]
    projected_data = centered_data @ pc_vectors
    
    print("\nTop 2 Eigenvalues (Variance):", values[:2])
    print("Projected Data (2D reduction, First 2 rows):\n", projected_data[:2])

if __name__ == "__main__":
    # Test Matrix
    A = np.array([
        [4, 1, 2],
        [2, 5, 1],
        [1, 1, 6]
    ], dtype=float)
    
    # 1. Recursive Det
    print(f"Recursive Det (Manual): {determinant_recursive(A)}")
    
    # 2. LU Det
    lu_det_demo(A)
    
    # 3. Verifications
    verify_decompositions(A)
    
    # 4. SVD via Eigen
    svd_via_eigen(A)
    
    # 5. PCA
    pca_demo()
