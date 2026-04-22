import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_cholesky():
    try:
        # 1. Get input values from the UI
        var_A = float(entry_var_A.get())
        var_B = float(entry_var_B.get())
        cov_AB = float(entry_cov_AB.get())

        # Prevent mathematical errors (The matrix must be Positive Definite)
        # Var(A) must be > 0 and the determinant must be > 0
        if var_A <= 0 or (var_A * var_B - cov_AB**2) <= 0:
            messagebox.showerror("Matrix Error", "The matrix must be Positive Definite!\nMake sure Var(A) > 0 and (Var(A)*Var(B) - Covariance^2) > 0.")
            return

        # 2. Create the Covariance Matrix (Symmetric 2x2 Matrix)
        Cov_Matrix = np.array([[var_A, cov_AB],
                               [cov_AB, var_B]])

        # 3. Calculate Cholesky Decomposition (Produces Lower Triangular Matrix 'L')
        L = np.linalg.cholesky(Cov_Matrix)

        # 4. Format the output text
        result_text = f"1. Covariance Matrix (Original):\n{Cov_Matrix}\n\n"
        result_text += f"2. Cholesky Matrix (L - Lower Triangular):\n{np.round(L, 4)}\n\n"
        
        # Multiply L by its Transpose (L^T) to verify it recreates the original matrix
        Reconstructed = np.dot(L, L.T)
        result_text += f"3. Verification (L * L^T):\n{np.round(Reconstructed, 4)}"

        # 5. Display the result on the UI
        label_result.config(text=result_text, fg="blue")

    except ValueError:
        # Handle cases where the user types letters instead of numbers
        messagebox.showerror("Input Error", "Please enter valid numbers!")
    except np.linalg.LinAlgError:
        # Handle backend linear algebra errors
        messagebox.showerror("Math Error", "Matrix calculation failed. Please check your inputs.")

# --- Main App Window Setup ---
app = tk.Tk()
app.title("Stock Market Risk Simulator 💸")
app.geometry("450x500")
app.config(padx=20, pady=20)

# App Title Label
title_label = tk.Label(app, text="Cholesky Decomposition", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# --- Inputs Section ---
frame_inputs = tk.Frame(app)
frame_inputs.pack(pady=10)

# Input 1: Variance of Stock A
tk.Label(frame_inputs, text="1. Variance of Stock A:").grid(row=0, column=0, sticky="w", pady=5)
entry_var_A = tk.Entry(frame_inputs, width=10)
entry_var_A.grid(row=0, column=1, pady=5)

# Input 2: Variance of Stock B
tk.Label(frame_inputs, text="2. Variance of Stock B:").grid(row=1, column=0, sticky="w", pady=5)
entry_var_B = tk.Entry(frame_inputs, width=10)
entry_var_B.grid(row=1, column=1, pady=5)

# Input 3: Covariance between Stock A and B
tk.Label(frame_inputs, text="3. Covariance (A & B):").grid(row=2, column=0, sticky="w", pady=5)
entry_cov_AB = tk.Entry(frame_inputs, width=10)
entry_cov_AB.grid(row=2, column=1, pady=5)

# --- Calculate Button ---
calc_button = tk.Button(app, text="Calculate Matrix 🚀", command=calculate_cholesky, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
calc_button.pack(pady=20)

# --- Result Display Section ---
label_result = tk.Label(app, text="Results will appear here...", font=("Courier", 11), justify="left")
label_result.pack(pady=10)

# Start the application loop
app.mainloop()