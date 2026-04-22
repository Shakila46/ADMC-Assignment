import tkinter as tk
from tkinter import messagebox
import numpy as np

# Function to calculate growth and display results
def calculate_growth():
    try:
        # 1. Get input values from the UI
        a11 = float(entry_a11.get())
        a12 = float(entry_a12.get())
        a21 = float(entry_a21.get())
        a22 = float(entry_a22.get())

        # 2. Create the 2x2 Matrix
        A = np.array([[a11, a12],
                      [a21, a22]])

        # 3. Calculate Eigenvalues and Eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(A)

        # 4. Format the output text
        result_text = f"Population Matrix:\n{A}\n\n"
        result_text += f"📈 Eigenvalues (Long-term growth rate):\n{np.round(eigenvalues, 4)}\n\n"
        result_text += f"📊 Eigenvectors (Ratio of juveniles and adults):\n{np.round(eigenvectors, 4)}"

        # 5. Update the UI with the result
        label_result.config(text=result_text, fg="blue")

    except ValueError:
        # Show an error message if the user enters letters instead of numbers
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# --- Main Application Window Setup ---
app = tk.Tk()
app.title("Population Growth Calculator 🐇")
app.geometry("450x550")
app.config(padx=20, pady=20)

# App Title Label
title_label = tk.Label(app, text="Population Growth Model", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# --- Input Section ---
frame_inputs = tk.Frame(app)
frame_inputs.pack(pady=10)

# Input 1: Offspring from juveniles
tk.Label(frame_inputs, text="1. Offspring from juveniles:").grid(row=0, column=0, sticky="w", pady=5)
entry_a11 = tk.Entry(frame_inputs, width=10)
entry_a11.grid(row=0, column=1, pady=5)

# Input 2: Offspring from adults
tk.Label(frame_inputs, text="2. Offspring from adults:").grid(row=1, column=0, sticky="w", pady=5)
entry_a12 = tk.Entry(frame_inputs, width=10)
entry_a12.grid(row=1, column=1, pady=5)

# Input 3: Survival rate (Juveniles -> Adults)
tk.Label(frame_inputs, text="3. Survival rate (Juveniles -> Adults):").grid(row=2, column=0, sticky="w", pady=5)
entry_a21 = tk.Entry(frame_inputs, width=10)
entry_a21.grid(row=2, column=1, pady=5)

# Input 4: Survival rate (Adults -> Next Year)
tk.Label(frame_inputs, text="4. Survival rate (Adults -> Next Year):").grid(row=3, column=0, sticky="w", pady=5)
entry_a22 = tk.Entry(frame_inputs, width=10)
entry_a22.grid(row=3, column=1, pady=5)

# --- Calculate Button ---
calc_button = tk.Button(app, text="Calculate Growth 🚀", command=calculate_growth, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
calc_button.pack(pady=20)

# --- Result Display Section ---
label_result = tk.Label(app, text="Results will appear here...", font=("Courier", 11), justify="left")
label_result.pack(pady=10)

# Start the application loop
app.mainloop()