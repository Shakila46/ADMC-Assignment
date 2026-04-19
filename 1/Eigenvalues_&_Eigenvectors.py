import math

print("========== PART 1: Eigenvalues & Eigenvectors ==========\n")

# 1. Get 9 values from the user
print("[ Please enter Symmetric values ]\n")
a11 = float(input("First Row,  First Column  (a11): "))
a12 = float(input("First Row,  Second Column (a12): "))
a13 = float(input("First Row,  Third Column  (a13): "))

a21 = float(input("Second Row, First Column  (a21): "))
a22 = float(input("Second Row, Second Column (a22): "))
a23 = float(input("Second Row, Third Column  (a23): "))

a31 = float(input("Third Row,  First Column  (a31): "))
a32 = float(input("Third Row,  Second Column (a32): "))
a33 = float(input("Third Row,  Third Column  (a33): "))

A = [[a11, a12, a13],
     [a21, a22, a23],
     [a31, a32, a33]]

try:
    # ==========================================
    # 2. FIND EIGENVALUES (Cardano's Formula)
    # ==========================================
    # The characteristic polynomial of a 3x3 matrix is:
    #   -λ³ + T·λ² - S·λ + D = 0
    # where T = trace, S = sum of 2x2 principal minors, D = determinant

    T = a11 + a22 + a33
    S = (a11*a22 - a12*a21) + (a11*a33 - a13*a31) + (a22*a33 - a23*a32)
    D = a11*(a22*a33 - a23*a32) - a12*(a21*a33 - a23*a31) + a13*(a21*a32 - a22*a31)

    # Rewrite as depressed cubic using substitution λ = t - a2/3
    a2, a1, a0 = -T, S, -D
    Q = (3 * a1 - a2**2) / 9.0
    R = (9 * a2 * a1 - 27 * a0 - 2 * (a2**3)) / 54.0

    # Clamp Q to avoid sqrt of positive number (symmetric matrices always have real eigenvalues)
    if Q >= 0:
        Q = -1e-8

    # Three real roots via trigonometric method
    theta = math.acos(max(min(R / math.sqrt(-(Q**3)), 1.0), -1.0))

    lambda1 = 2 * math.sqrt(-Q) * math.cos(theta / 3.0) - a2 / 3.0
    lambda2 = 2 * math.sqrt(-Q) * math.cos((theta + 2 * math.pi) / 3.0) - a2 / 3.0
    lambda3 = 2 * math.sqrt(-Q) * math.cos((theta + 4 * math.pi) / 3.0) - a2 / 3.0

    eigenvalues = [lambda1, lambda2, lambda3]

    print("\n✅ Eigenvalues:")
    print([round(l, 3) for l in eigenvalues])

    # ==========================================
    # 3. FIND EIGENVECTORS (Cross Product Method)
    # ==========================================
    # For each eigenvalue λ, build (A - λI).
    # Any two rows of (A - λI) span the null space plane.
    # Their cross product gives the eigenvector direction.
    # Cross product: row1 × row2 = (r1y*r2z - r1z*r2y,
    #                                r1z*r2x - r1x*r2z,
    #                                r1x*r2y - r1y*r2x)

    print("\n✅ Eigenvectors:")
    for lam in eigenvalues:
        # Build (A - λI): subtract λ only from diagonal entries
        M = [[A[i][j] - (lam if i == j else 0) for j in range(3)] for i in range(3)]

        r0, r1, r2 = M[0], M[1], M[2]

        # Cross product of Row 0 and Row 1
        vx = r0[1]*r1[2] - r0[2]*r1[1]
        vy = r0[2]*r1[0] - r0[0]*r1[2]
        vz = r0[0]*r1[1] - r0[1]*r1[0]

        mag = math.sqrt(vx**2 + vy**2 + vz**2)

        # If rows are parallel (zero cross product), try Row 0 and Row 2
        if mag < 0.0001:
            vx = r0[1]*r2[2] - r0[2]*r2[1]
            vy = r0[2]*r2[0] - r0[0]*r2[2]
            vz = r0[0]*r2[1] - r0[1]*r2[0]
            mag = math.sqrt(vx**2 + vy**2 + vz**2)

        # Normalize to unit vector
        if mag > 0:
            eig_vec = [vx/mag, vy/mag, vz/mag]
        else:
            eig_vec = [0.0, 0.0, 0.0]

        print(f"  For Eigenvalue {round(lam, 3):>8} -> {[round(v, 3) for v in eig_vec]}")

except Exception as e:
    print("\n❌ Error: Calculation failed. Please ensure you entered symmetric values.")