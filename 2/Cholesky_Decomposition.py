import math
print("--- 2x2 Cholesky Decomposition & Verification ---")
print("Please provide values for the Matrix (it must be Symmetric and Positive Definite.)\n")

# 1. Get 4 values from the user
a11 = float(input("First Row,  First Column  (a11): "))
a12 = float(input("First Row,  Second Column (a12): "))
a21 = float(input("Second Row, First Column  (a21): "))
a22 = float(input("Second Row, Second Column (a22): "))

# 2. Build the original 2x2 matrix A and empty result matrix L
A = [[a11, a12],
     [a21, a22]]

L = [[0.0, 0.0],
     [0.0, 0.0]]

try:
    # 3. Compute Cholesky Decomposition (find lower triangular matrix L)

    # -- First Column --
    # L[0][0] = sqrt(A[0][0])
    L[0][0] = math.sqrt(A[0][0])                          # BUG FIX: was math.sqrt(A) — need element [0][0], not the whole matrix

    # L[1][0] = A[1][0] / L[0][0]
    L[1][0] = A[1][0] / L[0][0]                           # BUG FIX: was L[1] = A[1] / L — need specific elements, not rows/matrix

    # -- Second Column --
    # L[1][1] = sqrt(A[1][1] - L[1][0]^2)
    L[1][1] = math.sqrt(A[1][1] - (L[1][0] ** 2))        # BUG FIX: was L[1] ** 2 — need element [1][0], not the whole row

    print("\n✅ 1. Lower Triangular Matrix (L):")
    for row in L:
        print([round(num, 3) for num in row])

    # 4. Compute the transpose of L (L^T) by swapping rows and columns
    L_T = [[0.0, 0.0],
           [0.0, 0.0]]
    for i in range(2):
        for j in range(2):
            L_T[j][i] = L[i][j]

    print("\n✅ 2. Upper Triangular Matrix (L^T):")
    for row in L_T:
        print([round(num, 3) for num in row])

    # 5. Verification: multiply L x L^T and confirm it equals the original matrix A
    A_check = [[0.0, 0.0],
               [0.0, 0.0]]

    # Standard matrix multiplication: A_check[i][j] = sum over k of L[i][k] * L_T[k][j]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                A_check[i][j] += L[i][k] * L_T[k][j]

    print("\n✅ 3. Verification (L x L^T = Original Matrix A):")
    for row in A_check:
        print([round(num, 3) for num in row])

# Error handling
except ValueError:
    print("\n❌ Error: The Matrix is not Positive Definite! (Cannot take the square root of a negative value.)")
except ZeroDivisionError:
    print("\n❌ Error: Division by zero occurred. Please provide different values.")