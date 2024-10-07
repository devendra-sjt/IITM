# import tkinter as tk
# from tkinter import messagebox
# import numpy as np
# import math

# class MathCalculatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Professional Math Calculator")
#         self.root.geometry("400x400")  # Initial window size

#         # Configure the grid to be responsive
#         for i in range(5):
#             self.root.grid_columnconfigure(i, weight=1)  # Allow columns to expand

#         # Matrix Size
#         self.matrix_size_label = tk.Label(root, text="Enter matrix size (2 or 3):", font=("Arial", 12))
#         self.matrix_size_label.grid(row=0, column=0, columnspan=4, pady=10)

#         self.matrix_size_entry = tk.Entry(root)
#         self.matrix_size_entry.grid(row=0, column=4)

#         self.generate_matrix_btn = tk.Button(root, text="Generate Matrix", command=self.generate_matrix_fields)
#         self.generate_matrix_btn.grid(row=1, column=0, columnspan=5, pady=10)

#         self.matrix_entries = []  # This will hold the entry widgets for matrix input

#         # Permutation and Combination Calculator UI
#         self.p_and_c_label = tk.Label(root, text="Permutation & Combination", font=("Arial", 14, "bold"))
#         self.p_and_c_label.grid(row=6, column=0, columnspan=5, pady=10)

#         self.n_label = tk.Label(root, text="Enter value of n:")
#         self.n_label.grid(row=7, column=0)
#         self.n_entry = tk.Entry(root)
#         self.n_entry.grid(row=7, column=1)

#         self.r_label = tk.Label(root, text="Enter value of r:")
#         self.r_label.grid(row=8, column=0)
#         self.r_entry = tk.Entry(root)
#         self.r_entry.grid(row=8, column=1)

#         self.calc_perm_btn = tk.Button(root, text="Calculate Permutation", command=self.calculate_permutation)
#         self.calc_perm_btn.grid(row=9, column=0, columnspan=2, pady=10)

#         self.calc_comb_btn = tk.Button(root, text="Calculate Combination", command=self.calculate_combination)
#         self.calc_comb_btn.grid(row=9, column=2, columnspan=2, pady=10)

#         # Result Label
#         self.result_label = tk.Label(root, text="", font=("Arial", 12))
#         self.result_label.grid(row=10, column=0, columnspan=5, pady=10)

#         self.calc_det_btn = tk.Button(root, text="Calculate Determinant", command=self.calculate_determinant)
#         self.calc_det_btn.grid(row=11, column=0, columnspan=5, pady=10)

#         # Button to Solve Matrix
#         self.solve_matrix_btn = tk.Button(root, text="Solve Matrix", command=self.solve_matrix)
#         self.solve_matrix_btn.grid(row=12, column=0, columnspan=5, pady=10)

#     def generate_matrix_fields(self):
#         # Clear previous entries
#         for widget in self.root.grid_slaves():
#             if int(widget.grid_info()["row"]) > 1 and int(widget.grid_info()["row"]) < 6:
#                 widget.destroy()

#         try:
#             size = int(self.matrix_size_entry.get())
#             if size not in [2, 3]:
#                 raise ValueError("Matrix size must be 2 or 3.")
#         except ValueError as e:
#             messagebox.showerror("Error", str(e))
#             return

#         self.matrix_entries.clear()
#         for i in range(size):
#             row_entries = []
#             for j in range(size):
#                 entry = tk.Entry(self.root, width=5)
#                 entry.grid(row=i + 2, column=j, padx=5, pady=5, sticky="nsew")  # Make entries expand
#                 row_entries.append(entry)
#             self.matrix_entries.append(row_entries)

#     def calculate_determinant(self):
#         try:
#             size = len(self.matrix_entries)
#             matrix = []
#             for row_entries in self.matrix_entries:
#                 row = [float(entry.get()) for entry in row_entries]
#                 matrix.append(row)

#             determinant = np.linalg.det(matrix)
#             self.result_label.config(text=f"Determinant: {determinant:.2f}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")

#     def solve_matrix(self):
#         try:
#             size = len(self.matrix_entries)
#             matrix = []
#             for row_entries in self.matrix_entries:
#                 row = [float(entry.get()) for entry in row_entries]
#                 matrix.append(row)

#             # Displaying the determinant (or other operations can be added)
#             determinant = np.linalg.det(matrix)
#             self.result_label.config(text=f"Determinant: {determinant:.2f}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")

#     def calculate_permutation(self):
#         try:
#             n = int(self.n_entry.get())
#             r = int(self.r_entry.get())
#             if n < 0 or r < 0 or r > n:
#                 raise ValueError("Invalid values for n and r!")
#             result = math.perm(n, r)
#             self.result_label.config(text=f"Permutation P({n}, {r}) = {result}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")

#     def calculate_combination(self):
#         try:
#             n = int(self.n_entry.get())
#             r = int(self.r_entry.get())
#             if n < 0 or r < 0 or r > n:
#                 raise ValueError("Invalid values for n and r!")
#             result = math.comb(n, r)
#             self.result_label.config(text=f"Combination C({n}, {r}) = {result}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")

# # Run the application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MathCalculatorApp(root)
#     root.mainloop()



# import tkinter as tk
# from tkinter import messagebox
# import math
# import numpy as np
# from sympy import symbols, Eq, solve, sympify

# class MathCalculatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Math Calculator")
#         self.root.configure(bg="#f0f0f0")

#         self.main_menu()

#     def main_menu(self):
#         """Display the main menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Select a task:", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)

#         tk.Button(self.root, text="Permutation & Combination", command=self.perm_comb_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Determinant (3x3 & 2x2)", command=self.determinant_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Quadratic Equation Solver", command=self.quadratic_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Linear Equation Solver", command=self.linear_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Factorial", command=self.factorial_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Prime Checker", command=self.prime_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="GCD & LCM", command=self.gcd_lcm_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=7, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Linear Equation Solver (3 Equations)", command=self.linear_3eq_menu, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=8, column=0, columnspan=2, pady=5)

#     def clear_frame(self):
#         """Clear all widgets in the frame."""
#         for widget in self.root.winfo_children():
#             widget.destroy()

#     def perm_comb_menu(self):
#         """Display the Permutation & Combination menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Permutation & Combination", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
#         tk.Label(self.root, text="Enter n:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
#         self.n_entry = tk.Entry(self.root)
#         self.n_entry.grid(row=1, column=1, pady=5)

#         tk.Label(self.root, text="Enter r:", bg="#f0f0f0").grid(row=2, column=0, pady=5)
#         self.r_entry = tk.Entry(self.root)
#         self.r_entry.grid(row=2, column=1, pady=5)

#         tk.Button(self.root, text="Calculate Permutation", command=self.calculate_permutation, bg="#2196F3", fg="white").grid(row=3, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Calculate Combination", command=self.calculate_combination, bg="#2196F3", fg="white").grid(row=4, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=5, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=6, column=0, columnspan=2, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter non-negative integers for n and r.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=8, column=0, columnspan=2, pady=5)

#     def determinant_menu(self):
#         """Display the Determinant menu."""
#         self.clear_frame()

#         # 3x3 Matrix Determinant Section
#         self.matrix_3x3_entries = []
#         tk.Label(self.root, text="3x3 Matrix Determinant", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=3, pady=10)
#         for i in range(3):
#             row_entries = []
#             for j in range(3):
#                 entry = tk.Entry(self.root, width=5)
#                 entry.grid(row=1 + i, column=j, pady=5)
#                 row_entries.append(entry)
#             self.matrix_3x3_entries.append(row_entries)

#         self.det_3x3_button = tk.Button(self.root, text="Calculate 3x3 Determinant", command=self.calculate_determinant_3x3, bg="#2196F3", fg="white")
#         self.det_3x3_button.grid(row=4, column=0, columnspan=3, pady=5)

#         # 2x2 Matrix Determinant Section
#         self.matrix_2x2_entries = []
#         tk.Label(self.root, text="2x2 Matrix Determinant", font=("Helvetica", 16), bg="#f0f0f0").grid(row=5, column=0, columnspan=2, pady=10)
#         for i in range(2):
#             row_entries = []
#             for j in range(2):
#                 entry = tk.Entry(self.root, width=5)
#                 entry.grid(row=6 + i, column=j, pady=5)
#                 row_entries.append(entry)
#             self.matrix_2x2_entries.append(row_entries)

#         self.det_2x2_button = tk.Button(self.root, text="Calculate 2x2 Determinant", command=self.calculate_determinant_2x2, bg="#2196F3", fg="white")
#         self.det_2x2_button.grid(row=8, column=0, columnspan=2, pady=5)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=9, column=0, columnspan=3, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=10, column=0, columnspan=3, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=11, column=0, columnspan=3, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter numbers in the matrix fields.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=12, column=0, columnspan=3, pady=5)

#     def quadratic_menu(self):
#         """Display the Quadratic Equation Solver menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Quadratic Equation Solver", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=3, pady=10)
#         self.a_entry = tk.Entry(self.root, width=5)
#         self.a_entry.grid(row=1, column=0, pady=5)
#         self.b_entry = tk.Entry(self.root, width=5)
#         self.b_entry.grid(row=1, column=1, pady=5)
#         self.c_entry = tk.Entry(self.root, width=5)
#         self.c_entry.grid(row=1, column=2, pady=5)

#         self.quad_button = tk.Button(self.root, text="Solve Quadratic", command=self.solve_quadratic, bg="#2196F3", fg="white")
#         self.quad_button.grid(row=2, column=0, columnspan=3, pady=5)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=3, column=0, columnspan=3, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=4, column=0, columnspan=3, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=5, column=0, columnspan=3, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter coefficients a, b, and c for ax^2 + bx + c = 0.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=6, column=0, columnspan=3, pady=5)

#     def linear_menu(self):
#         """Display the Linear Equation Solver menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Linear Equation Solver", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=3, pady=10)
#         self.eq1_entry = tk.Entry(self.root, width=20)
#         self.eq1_entry.grid(row=1, column=0, columnspan=3, pady=5)
#         self.eq2_entry = tk.Entry(self.root, width=20)
#         self.eq2_entry.grid(row=2, column=0, columnspan=3, pady=5)

#         self.linear_button = tk.Button(self.root, text="Solve Linear Equations", command=self.solve_linear, bg="#2196F3", fg="white")
#         self.linear_button.grid(row=3, column=0, columnspan=3, pady=5)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=4, column=0, columnspan=3, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=5, column=0, columnspan=3, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=6, column=0, columnspan=3, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter equations in the form 'ax + by = c'.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=7, column=0, columnspan=3, pady=5)

#     def factorial_menu(self):
#         """Display the Factorial menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Factorial Calculation", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
#         tk.Label(self.root, text="Enter a number:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
#         self.fact_entry = tk.Entry(self.root)
#         self.fact_entry.grid(row=1, column=1, pady=5)

#         self.fact_button = tk.Button(self.root, text="Calculate Factorial", command=self.calculate_factorial, bg="#2196F3", fg="white")
#         self.fact_button.grid(row=2, column=0, columnspan=2, pady=5)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=3, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=4, column=0, columnspan=2, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter a non-negative integer.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=6, column=0, columnspan=2, pady=5)

#     def prime_menu(self):
#         """Display the Prime Checker menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Prime Number Checker", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
#         tk.Label(self.root, text="Enter a number:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
#         self.prime_entry = tk.Entry(self.root)
#         self.prime_entry.grid(row=1, column=1, pady=5)

#         self.prime_button = tk.Button(self.root, text="Check Prime", command=self.check_prime, bg="#2196F3", fg="white")
#         self.prime_button.grid(row=2, column=0, columnspan=2, pady=5)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=3, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=4, column=0, columnspan=2, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter a positive integer.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=6, column=0, columnspan=2, pady=5)

#     def gcd_lcm_menu(self):
#         """Display the GCD & LCM menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="GCD & LCM Calculation", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
#         tk.Label(self.root, text="Enter first number:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
#         self.gcd_lcm_entry1 = tk.Entry(self.root)
#         self.gcd_lcm_entry1.grid(row=1, column=1, pady=5)

#         tk.Label(self.root, text="Enter second number:", bg="#f0f0f0").grid(row=2, column=0, pady=5)
#         self.gcd_lcm_entry2 = tk.Entry(self.root)
#         self.gcd_lcm_entry2.grid(row=2, column=1, pady=5)

#         self.gcd_button = tk.Button(self.root, text="Calculate GCD", command=self.calculate_gcd, bg="#2196F3", fg="white")
#         self.gcd_button.grid(row=3, column=0, columnspan=2, pady=5)

#         self.lcm_button = tk.Button(self.root, text="Calculate LCM", command=self.calculate_lcm, bg="#2196F3", fg="white")
#         self.lcm_button.grid(row=4, column=0, columnspan=2, pady=5)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=5, column=0, columnspan=2, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=6, column=0, columnspan=2, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter two positive integers.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=8, column=0, columnspan=2, pady=5)

#     def get_input_values(self):
#         """Retrieve and validate input values."""
#         try:
#             n = int(self.n_entry.get())
#             r = int(self.r_entry.get())
#             if n < 0 or r < 0 or r > n:
#                 raise ValueError("Invalid values for n and r!")
#             return n, r
#         except ValueError as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")
#             return None, None

#     def calculate_permutation(self):
#         """Calculate and display the permutation."""
#         n, r = self.get_input_values()
#         if n is not None and r is not None:
#             result = math.perm(n, r)
#             self.result_label.config(text=f"Permutation P({n}, {r}) = {result}")

#     def calculate_combination(self):
#         """Calculate and display the combination."""
#         n, r = self.get_input_values()
#         if n is not None and r is not None:
#             result = math.comb(n, r)
#             self.result_label.config(text=f"Combination C({n}, {r}) = {result}")

#     def calculate_determinant_3x3(self):
#         """Calculate and display the determinant of a 3x3 matrix."""
#         try:
#             matrix = []
#             for row_entries in self.matrix_3x3_entries:
#                 row = [float(entry.get()) for entry in row_entries]
#                 matrix.append(row)
#             matrix = np.array(matrix)
#             det = np.linalg.det(matrix)
#             self.result_label.config(text=f"3x3 Determinant = {det:.2f}")
#         except ValueError:
#             messagebox.showerror("Error", "Invalid matrix input!")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def calculate_determinant_2x2(self):
#         """Calculate and display the determinant of a 2x2 matrix."""
#         try:
#             matrix = []
#             for row_entries in self.matrix_2x2_entries:
#                 row = [float(entry.get()) for entry in row_entries]
#                 matrix.append(row)
#             matrix = np.array(matrix)
#             det = np.linalg.det(matrix)
#             self.result_label.config(text=f"2x2 Determinant = {det:.2f}")
#         except ValueError:
#             messagebox.showerror("Error", "Invalid matrix input!")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def solve_quadratic(self):
#         """Solve and display the roots of a quadratic equation."""
#         try:
#             a = float(self.a_entry.get())
#             b = float(self.b_entry.get())
#             c = float(self.c_entry.get())
#             discriminant = b**2 - 4*a*c
#             if discriminant > 0:
#                 root1 = (-b + math.sqrt(discriminant)) / (2*a)
#                 root2 = (-b - math.sqrt(discriminant)) / (2*a)
#                 self.result_label.config(text=f"Roots: {root1:.2f}, {root2:.2f}")
#             elif discriminant == 0:
#                 root = -b / (2*a)
#                 self.result_label.config(text=f"Root: {root:.2f}")
#             else:
#                 self.result_label.config(text="No real roots")
#         except ValueError:
#             messagebox.showerror("Error", "Invalid input for quadratic equation!")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def solve_linear(self):
#         """Solve and display the solution of two linear equations."""
#         try:
#             x, y = symbols('x y')
#             eq1 = Eq(sympify(self.eq1_entry.get()))
#             eq2 = Eq(sympify(self.eq2_entry.get()))
#             solution = solve((eq1, eq2), (x, y))
#             self.result_label.config(text=f"Solution: x = {solution[x]}, y = {solution[y]}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def calculate_factorial(self):
#         """Calculate and display the factorial of a number."""
#         try:
#             num = int(self.fact_entry.get())
#             if num < 0:
#                 raise ValueError("Number must be non-negative!")
#             result = math.factorial(num)
#             self.result_label.config(text=f"Factorial of {num} = {result}")
#         except ValueError as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def check_prime(self):
#         """Check and display if a number is prime."""
#         try:
#             num = int(self.prime_entry.get())
#             if num <= 1:
#                 result = f"{num} is not a prime number"
#             else:
#                 for i in range(2, int(math.sqrt(num)) + 1):
#                     if num % i == 0:
#                         result = f"{num} is not a prime number"
#                         break
#                 else:
#                     result = f"{num} is a prime number"
#             self.result_label.config(text=result)
#         except ValueError as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def calculate_gcd(self):
#         """Calculate and display the GCD of two numbers."""
#         try:
#             num1 = int(self.gcd_lcm_entry1.get())
#             num2 = int(self.gcd_lcm_entry2.get())
#             result = math.gcd(num1, num2)
#             self.result_label.config(text=f"GCD of {num1} and {num2} = {result}")
#         except ValueError as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def calculate_lcm(self):
#         """Calculate and display the LCM of two numbers."""
#         try:
#             num1 = int(self.gcd_lcm_entry1.get())
#             num2 = int(self.gcd_lcm_entry2.get())
#             result = abs(num1 * num2) // math.gcd(num1, num2)
#             self.result_label.config(text=f"LCM of {num1} and {num2} = {result}")
#         except ValueError as e:
#             messagebox.showerror("Error", f"Invalid input: {e}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")


#     def linear_3eq_menu(self):
#         """Display the Linear Equation Solver menu for 3 equations."""
#         self.clear_frame()

#         tk.Label(self.root, text="Linear Equation Solver (3 Equations)", font=("Helvetica", 16), bg="#f0f0f0").grid(row=0, column=0, columnspan=3, pady=10)
#         self.eq1_entry = tk.Entry(self.root, width=20)
#         self.eq1_entry.grid(row=1, column=0, columnspan=3, pady=5)
#         self.eq2_entry = tk.Entry(self.root, width=20)
#         self.eq2_entry.grid(row=2, column=0, columnspan=3, pady=5)
#         self.eq3_entry = tk.Entry(self.root, width=20)
#         self.eq3_entry.grid(row=3, column=0, columnspan=3, pady=5)

#         self.linear_3eq_button = tk.Button(self.root, text="Solve 3 Equations", command=self.solve_linear_3eq, bg="#2196F3", fg="white")
#         self.linear_3eq_button.grid(row=4, column=0, columnspan=3, pady=5)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white").grid(row=5, column=0, columnspan=3, pady=5)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white").grid(row=6, column=0, columnspan=3, pady=5)

#         self.result_label = tk.Label(self.root, text="", bg="#f0f0f0")
#         self.result_label.grid(row=7, column=0, columnspan=3, pady=10)

#         self.instruction_label = tk.Label(self.root, text="Instructions: Enter equations like '2*x + 3*y - z = 4'.", font=("Helvetica", 10), bg="#f0f0f0", fg="blue")
#         self.instruction_label.grid(row=8, column=0, columnspan=3, pady=5)

#     def solve_linear_3eq(self):
#         """Solve and display the solution of three linear equations."""
#         try:
#             # Validate input
#             x, y, z = symbols('x y z')
#             eq1_str = self.eq1_entry.get()
#             eq2_str = self.eq2_entry.get()
#             eq3_str = self.eq3_entry.get()

#             # Ensure equations are in the correct format
#             if not all([eq1_str, eq2_str, eq3_str]):
#                 raise ValueError("Please enter all three equations.")

#             eq1 = Eq(sympify(eq1_str))
#             eq2 = Eq(sympify(eq2_str))
#             eq3 = Eq(sympify(eq3_str))

#             # Solve the equations
#             solution = solve((eq1, eq2, eq3), (x, y, z))

#             # Display the result
#             self.result_label.config(text=f"Solution: x = {solution[x]}, y = {solution[y]}, z = {solution[z]}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

#     def reset_inputs(self):
#         """Reset the input fields."""
#         for widget in self.root.winfo_children():
#             if isinstance(widget, tk.Entry):
#                 widget.delete(0, tk.END)

# # Run the application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MathCalculatorApp(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# from sympy import symbols, Eq, sympify, solve

# class MathCalculatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Math Calculator")
#         self.root.geometry("450x500")
#         self.root.config(bg="#e0e0e0")

#         self.main_menu()

#     def clear_frame(self):
#         """Clear the window frame."""
#         for widget in self.root.winfo_children():
#             widget.destroy()

#     def main_menu(self):
#         """Display the main menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Math Calculator", font=("Helvetica", 18, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

#         # Menu buttons
#         tk.Button(self.root, text="Permutation & Combination", command=self.perm_comb_menu, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=1, column=0, columnspan=2, pady=10, padx=10)
#         tk.Button(self.root, text="Linear Equations Solver", command=self.linear_equation_menu, font=("Helvetica", 12), bg="#2196F3", fg="white").grid(row=2, column=0, columnspan=2, pady=10, padx=10)

#     def perm_comb_menu(self):
#         """Display the Permutation & Combination menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Permutation & Combination", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

#         tk.Label(self.root, text="Enter n:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
#         self.n_entry = tk.Entry(self.root, font=("Helvetica", 12))
#         self.n_entry.grid(row=1, column=1, pady=5, padx=10)

#         tk.Label(self.root, text="Enter r:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=10)
#         self.r_entry = tk.Entry(self.root, font=("Helvetica", 12))
#         self.r_entry.grid(row=2, column=1, pady=5, padx=10)

#         tk.Button(self.root, text="Calculate Permutation P(n,r)", command=self.calculate_permutation, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
#         tk.Button(self.root, text="Calculate Combination C(n,r)", command=self.calculate_combination, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=5, padx=10)

#         self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
#         self.result_label.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

#     def linear_equation_menu(self):
#         """Display the Linear Equations Solver menu."""
#         self.clear_frame()

#         tk.Label(self.root, text="Linear Equations Solver", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=3, pady=10, padx=10)

#         tk.Label(self.root, text="Solve 2x2 System", font=("Helvetica", 14), bg="#e0e0e0").grid(row=1, column=0, columnspan=3, pady=5, padx=10)
#         self.eq1_2x2_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
#         self.eq1_2x2_entry.grid(row=2, column=0, columnspan=3, pady=5, padx=10)
#         self.eq2_2x2_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
#         self.eq2_2x2_entry.grid(row=3, column=0, columnspan=3, pady=5, padx=10)

#         tk.Button(self.root, text="Solve 2 Equations", command=self.solve_linear_2eq, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=3, pady=5, padx=10)

#         tk.Label(self.root, text="Solve 3x3 System", font=("Helvetica", 14), bg="#e0e0e0").grid(row=5, column=0, columnspan=3, pady=5, padx=10)
#         self.eq1_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
#         self.eq1_3x3_entry.grid(row=6, column=0, columnspan=3, pady=5, padx=10)
#         self.eq2_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
#         self.eq2_3x3_entry.grid(row=7, column=0, columnspan=3, pady=5, padx=10)
#         self.eq3_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
#         self.eq3_3x3_entry.grid(row=8, column=0, columnspan=3, pady=5, padx=10)

#         tk.Button(self.root, text="Solve 3 Equations", command=self.solve_linear_3eq, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=9, column=0, columnspan=3, pady=5, padx=10)

#         tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=10, column=0, columnspan=3, pady=5, padx=10)
#         tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=11, column=0, columnspan=3, pady=5, padx=10)

#         self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
#         self.result_label.grid(row=12, column=0, columnspan=3, pady=10, padx=10)

#     def solve_linear_2eq(self):
#         """Solve and display the solution for 2 linear equations."""
#         try:
#             x, y = symbols('x y')
#             eq1_str = self.eq1_2x2_entry.get()
#             eq2_str = self.eq2_2x2_entry.get()

#             if not eq1_str or not eq2_str:
#                 raise ValueError("Both equations must be entered.")

#             eq1 = Eq(sympify(eq1_str))
#             eq2 = Eq(sympify(eq2_str))

#             solution = solve((eq1, eq2), (x, y))
#             self.result_label.config(text=f"Solution: x = {solution[x]}, y = {solution[y]}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Error solving 2 equations: {e}")

#     def solve_linear_3eq(self):
#         """Solve and display the solution of three linear equations."""
#         try:
#             x, y, z = symbols('x y z')
#             eq1_str = self.eq1_3x3_entry.get()
#             eq2_str = self.eq2_3x3_entry.get()
#             eq3_str = self.eq3_3x3_entry.get()

#             if not eq1_str or not eq2_str or not eq3_str:
#                 raise ValueError("All three equations must be entered.")

#             eq1 = Eq(sympify(eq1_str))
#             eq2 = Eq(sympify(eq2_str))
#             eq3 = Eq(sympify(eq3_str))

#             solution = solve((eq1, eq2, eq3), (x, y, z))
#             self.result_label.config(text=f"Solution: x = {solution[x]}, y = {solution[y]}, z = {solution[z]}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Error solving 3 equations: {e}")

#     def calculate_permutation(self):
#         """Calculate and display the permutation."""
#         try:
#             n = int(self.n_entry.get())
#             r = int(self.r_entry.get())

#             if n < 0 or r < 0:
#                 raise ValueError("n and r must be non-negative integers.")
#             if r > n:
#                 raise ValueError("r cannot be greater than n.")

#             perm = self.factorial(n) // self.factorial(n - r)
#             self.result_label.config(text=f"Permutation (P({n},{r})) = {perm}")
#         except ValueError as e:
#             messagebox.showerror("Error", str(e))

#     def calculate_combination(self):
#         """Calculate and display the combination."""
#         try:
#             n = int(self.n_entry.get())
#             r = int(self.r_entry.get())

#             if n < 0 or r < 0:
#                 raise ValueError("n and r must be non-negative integers.")
#             if r > n:
#                 raise ValueError("r cannot be greater than n.")

#             comb = self.factorial(n) // (self.factorial(r) * self.factorial(n - r))
#             self.result_label.config(text=f"Combination (C({n},{r})) = {comb}")
#         except ValueError as e:
#             messagebox.showerror("Error", str(e))

#     def factorial(self, num):
#         """Return the factorial of a number."""
#         if num == 0 or num == 1:
#             return 1
#         else:
#             return num * self.factorial(num - 1)

#     def reset_inputs(self):
#         """Clear all input fields and result labels."""
#         self.n_entry.delete(0, tk.END)
#         self.r_entry.delete(0, tk.END)
#         self.eq1_2x2_entry.delete(0, tk.END)
#         self.eq2_2x2_entry.delete(0, tk.END)
#         self.eq1_3x3_entry.delete(0, tk.END)
#         self.eq2_3x3_entry.delete(0, tk.END)
#         self.eq3_3x3_entry.delete(0, tk.END)
#         self.result_label.config(text="")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MathCalculatorApp(root)
#     root.mainloop()













# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------








import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Eq, sympify, solve, Matrix
import math

class MathCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Calculator")
        self.root.geometry("500x600")
        self.root.config(bg="#e0e0e0")

        self.main_menu()

    def clear_frame(self):
        """Clear the window frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        """Display the main menu."""
        self.clear_frame()

        tk.Label(self.root, text="Math Calculator", font=("Helvetica", 18, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Menu buttons
        tk.Button(self.root, text="Permutation & Combination", command=self.perm_comb_menu, font=("Helvetica", 12), bg="#4CAF50", fg="white").grid(row=1, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Linear Equations Solver", command=self.linear_equation_menu, font=("Helvetica", 12), bg="#2196F3", fg="white").grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Factorial Calculator", command=self.factorial_menu, font=("Helvetica", 12), bg="#FF9800", fg="white").grid(row=3, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Prime Number Checker", command=self.prime_menu, font=("Helvetica", 12), bg="#FFC107", fg="white").grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Quadratic Equation Solver", command=self.quadratic_menu, font=("Helvetica", 12), bg="#9C27B0", fg="white").grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="Determinant Calculator", command=self.determinant_menu, font=("Helvetica", 12), bg="#673AB7", fg="white").grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        tk.Button(self.root, text="GCD & LCM Calculator", command=self.gcd_lcm_menu, font=("Helvetica", 12), bg="#3F51B5", fg="white").grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    def perm_comb_menu(self):
        """Display the Permutation & Combination menu."""
        self.clear_frame()

        tk.Label(self.root, text="Permutation & Combination", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter n:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.n_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.n_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter r:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=10)
        self.r_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.r_entry.grid(row=2, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Calculate Permutation P(n,r)", command=self.calculate_permutation, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Calculate Combination C(n,r)", command=self.calculate_combination, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    def linear_equation_menu(self):
        """Display the Linear Equations Solver menu."""
        self.clear_frame()

        tk.Label(self.root, text="Linear Equations Solver", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        tk.Label(self.root, text="Solve 2x2 System", font=("Helvetica", 14), bg="#e0e0e0").grid(row=1, column=0, columnspan=3, pady=5, padx=10)
        self.eq1_2x2_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq1_2x2_entry.grid(row=2, column=0, columnspan=3, pady=5, padx=10)
        self.eq2_2x2_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq2_2x2_entry.grid(row=3, column=0, columnspan=3, pady=5, padx=10)

        tk.Button(self.root, text="Solve 2 Equations", command=self.solve_linear_2eq, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=3, pady=5, padx=10)

        tk.Label(self.root, text="Solve 3x3 System", font=("Helvetica", 14), bg="#e0e0e0").grid(row=5, column=0, columnspan=3, pady=5, padx=10)
        self.eq1_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq1_3x3_entry.grid(row=6, column=0, columnspan=3, pady=5, padx=10)
        self.eq2_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq2_3x3_entry.grid(row=7, column=0, columnspan=3, pady=5, padx=10)
        self.eq3_3x3_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.eq3_3x3_entry.grid(row=8, column=0, columnspan=3, pady=5, padx=10)

        tk.Button(self.root, text="Solve 3 Equations", command=self.solve_linear_3eq, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=9, column=0, columnspan=3, pady=5, padx=10)

        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=10, column=0, columnspan=3, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=11, column=0, columnspan=3, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=12, column=0, columnspan=3, pady=10, padx=10)

    def factorial_menu(self):
        """Display the Factorial Calculator menu."""
        self.clear_frame()

        tk.Label(self.root, text="Factorial Calculator", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter a non-negative integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.factorial_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.factorial_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Calculate Factorial", command=self.calculate_factorial, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def prime_menu(self):
        """Display the Prime Number Checker menu."""
        self.clear_frame()

        tk.Label(self.root, text="Prime Number Checker", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter an integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.prime_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.prime_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Check if Prime", command=self.check_prime, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def quadratic_menu(self):
        """Display the Quadratic Equation Solver menu."""
        self.clear_frame()

        tk.Label(self.root, text="Quadratic Equation Solver", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        tk.Label(self.root, text="Enter a:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.a_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.a_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter b:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=10)
        self.b_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.b_entry.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter c:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=3, column=0, pady=5, padx=10)
        self.c_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.c_entry.grid(row=3, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Solve Quadratic", command=self.solve_quadratic, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    def determinant_menu(self):
        """Display the 3x3 Determinant Calculator menu."""
        self.clear_frame()

        tk.Label(self.root, text="Determinant Calculator (3x3)", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        # Create a grid for the 3x3 matrix
        self.matrix_entries_3x3 = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(self.root, font=("Helvetica", 12), width=5)
                entry.grid(row=i + 1, column=j, pady=5, padx=5)
                row_entries.append(entry)
            self.matrix_entries_3x3.append(row_entries)

        tk.Button(self.root, text="Calculate Determinant", command=self.calculate_determinant_3x3, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=3, pady=5, padx=10)
        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=3, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=3, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=7, column=0, columnspan=3, pady=10, padx=10)


    def gcd_lcm_menu(self):
        """Display the GCD & LCM Calculator menu."""
        self.clear_frame()

        tk.Label(self.root, text="GCD & LCM Calculator", font=("Helvetica", 16, "bold"), bg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.root, text="Enter first integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=1, column=0, pady=5, padx=10)
        self.gcd_lcm_entry1 = tk.Entry(self.root, font=("Helvetica", 12))
        self.gcd_lcm_entry1.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(self.root, text="Enter second integer:", font=("Helvetica", 12), bg="#e0e0e0").grid(row=2, column=0, pady=5, padx=10)
        self.gcd_lcm_entry2 = tk.Entry(self.root, font=("Helvetica", 12))
        self.gcd_lcm_entry2.grid(row=2, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Calculate GCD", command=self.calculate_gcd, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, pady=5, padx=10)
        tk.Button(self.root, text="Calculate LCM", command=self.calculate_lcm, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=3, column=1, pady=5, padx=10)

        tk.Button(self.root, text="Clear Input", command=self.reset_inputs, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=5, padx=10)
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#9E9E9E", fg="white", font=("Helvetica", 12)).grid(row=5, column=0, columnspan=2, pady=5, padx=10)

        self.result_label = tk.Label(self.root, text="", bg="#e0e0e0", font=("Helvetica", 12))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    def reset_inputs(self):
        """Clear all input fields and result labels."""
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            if isinstance(widget, tk.Label) and "result" in widget.cget("text"):
                widget.config(text="")

    def calculate_permutation(self):
        """Calculate permutation P(n, r)."""
        n = int(self.n_entry.get())
        r = int(self.r_entry.get())
        result = math.perm(n, r)
        self.result_label.config(text=f"P({n},{r}) = {result}")

    def calculate_combination(self):
        """Calculate combination C(n, r)."""
        n = int(self.n_entry.get())
        r = int(self.r_entry.get())
        result = math.comb(n, r)
        self.result_label.config(text=f"C({n},{r}) = {result}")

    def solve_linear_2eq(self):
        """Solve a system of 2 linear equations."""
        eq1 = self.eq1_2x2_entry.get()
        eq2 = self.eq2_2x2_entry.get()
        try:
            x, y = symbols('x y')
            equations = [sympify(eq1.replace('=', '-(') + ')'), sympify(eq2.replace('=', '-(') + ')')]
            solutions = solve(equations, (x, y))
            self.result_label.config(text=f"Solutions: x = {solutions[x]}, y = {solutions[y]}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid equation format.")

    def solve_linear_3eq(self):
        """Solve a system of 3 linear equations."""
        eq1 = self.eq1_3x3_entry.get()
        eq2 = self.eq2_3x3_entry.get()
        eq3 = self.eq3_3x3_entry.get()
        try:
            x, y, z = symbols('x y z')
            equations = [sympify(eq1.replace('=', '-(') + ')'), sympify(eq2.replace('=', '-(') + ')'), sympify(eq3.replace('=', '-(') + ')')]
            solutions = solve(equations, (x, y, z))
            self.result_label.config(text=f"Solutions: x = {solutions[x]}, y = {solutions[y]}, z = {solutions[z]}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid equation format.")

    def calculate_factorial(self):
        """Calculate factorial of a number."""
        try:
            number = int(self.factorial_entry.get())
            if number < 0:
                raise ValueError("Negative value")
            result = math.factorial(number)
            self.result_label.config(text=f"{number}! = {result}")
        except Exception:
            messagebox.showerror("Error", "Please enter a non-negative integer.")

    def check_prime(self):
        """Check if a number is prime."""
        try:
            number = int(self.prime_entry.get())
            if number <= 1:
                result = "Not Prime"
            else:
                result = "Prime" if all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1)) else "Not Prime"
            self.result_label.config(text=f"{number} is {result}.")
        except Exception:
            messagebox.showerror("Error", "Please enter an integer.")

    def solve_quadratic(self):
        """Solve a quadratic equation."""
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                self.result_label.config(text="No real roots.")
            elif discriminant == 0:
                root = -b / (2*a)
                self.result_label.config(text=f"One root: {root}")
            else:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                self.result_label.config(text=f"Roots: {root1}, {root2}")
        except Exception:
            messagebox.showerror("Error", "Invalid input values.")


    def calculate_determinant_3x3(self):
        """Calculate determinant of a 3x3 matrix."""
        try:
            a11 = float(self.matrix_entries_3x3[0][0].get())
            a12 = float(self.matrix_entries_3x3[0][1].get())
            a13 = float(self.matrix_entries_3x3[0][2].get())
            a21 = float(self.matrix_entries_3x3[1][0].get())
            a22 = float(self.matrix_entries_3x3[1][1].get())
            a23 = float(self.matrix_entries_3x3[1][2].get())
            a31 = float(self.matrix_entries_3x3[2][0].get())
            a32 = float(self.matrix_entries_3x3[2][1].get())
            a33 = float(self.matrix_entries_3x3[2][2].get())

            # Calculate the determinant of the 3x3 matrix
            determinant = (a11 * (a22 * a33 - a23 * a32) -
                        a12 * (a21 * a33 - a23 * a31) +
                        a13 * (a21 * a32 - a22 * a31))
            
            self.result_label.config(text=f"Determinant = {determinant}")
        except ValueError:
            messagebox.showerror("Error", "Invalid matrix format.")


    def calculate_gcd(self):
        """Calculate GCD of two numbers."""
        try:
            num1 = int(self.gcd_lcm_entry1.get())
            num2 = int(self.gcd_lcm_entry2.get())
            result = math.gcd(num1, num2)
            self.result_label.config(text=f"GCD({num1}, {num2}) = {result}")
        except Exception:
            messagebox.showerror("Error", "Please enter valid integers.")

    def calculate_lcm(self):
        """Calculate LCM of two numbers."""
        try:
            num1 = int(self.gcd_lcm_entry1.get())
            num2 = int(self.gcd_lcm_entry2.get())
            result = abs(num1 * num2) // math.gcd(num1, num2)
            self.result_label.config(text=f"LCM({num1}, {num2}) = {result}")
        except Exception:
            messagebox.showerror("Error", "Please enter valid integers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathCalculatorApp(root)
    root.mainloop()
