import math
print("========== PART 1: Eigenvalues & Eigenvectors (2x2) ==========\n")

# 1. Get 4 values from the user
print("[ Please enter Symmetric values ]\n")
a11 = float(input("First Row,  First Column  (a11): "))
a12 = float(input("First Row,  Second Column (a12): "))
a21 = float(input("Second Row, First Column  (a21): "))
a22 = float(input("Second Row, Second Column (a22): "))

A = [[a11, a12],
     [a21, a22]]

try:
    # ==========================================
    # 2. FIND EIGENVALUES (Quadratic Formula)
    # ==========================================
    # Characteristic equation of a 2x2 Matrix: λ² - Tλ + D = 0

    T = a11 + a22                  # Trace (sum of diagonal elements)
    D = (a11 * a22) - (a12 * a21)  # Determinant

    # Discriminant part: b² - 4ac
    discriminant = T**2 - 4 * D

    # For positive definite (Symmetric) matrices, discriminant cannot be negative.
    # Small check to avoid floating point errors:
    if discriminant < 0:
        discriminant = 0

    # Find the 2 roots using the quadratic formula
    lambda1 = (T + math.sqrt(discriminant)) / 2.0
    lambda2 = (T - math.sqrt(discriminant)) / 2.0
    eigenvalues = [lambda1, lambda2]

    print("\n✅ Eigenvalues:")
    print([round(l, 3) for l in eigenvalues])

    # ==========================================
    # 3. FIND EIGENVECTORS (Orthogonal Vector Method)
    # ==========================================
    print("\n✅ Eigenvectors:")
    for lam in eigenvalues:
        # Build the (A - λI) matrix
        M = [[A[i][j] - (lam if i == j else 0) for j in range(2)] for i in range(2)]

        r0 = M[0]  # First row of (A - λI)
        r1 = M[1]  # Second row of (A - λI)

        # In 2D, the perpendicular (orthogonal) vector to [a, b] is [-b, a].
        # Use the first row to find the eigenvector:
        vx = -r0[1]
        vy =  r0[0]

        mag = math.sqrt(vx**2 + vy**2)

        # If the first row is all zeros, fall back to the second row
        if mag < 0.0001:
            vx = -r1[1]
            vy =  r1[0]
            mag = math.sqrt(vx**2 + vy**2)

        # Normalize to get a unit vector
        if mag > 0:
            eig_vec = [vx / mag, vy / mag]
        else:
            # Default vector for edge cases like the identity matrix
            eig_vec = [1.0, 0.0]

        print(f"  For Eigenvalue {round(lam, 3):>8} -> {[round(v, 3) for v in eig_vec]}")

except Exception as e:
    print("\n❌ Error: Calculation failed. Please ensure you entered symmetric values.")
    print(f"   Detail: {e}")