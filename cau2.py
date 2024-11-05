import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff, integrate, Eq, solve
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Phần mềm Hỗ trợ học tập môn Giải tích")


# Hàm tính đạo hàm
def calculate_derivative():
    try:
        func = entry_function.get()  # Lấy hàm người dùng nhập
        x = symbols('x')
        f = eval(func)  # Biểu thức hàm người dùng nhập
        derivative = diff(f, x)
        result_derivative.set(f"Đạo hàm: {derivative}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")


# Hàm tính tích phân
def calculate_integral():
    try:
        func = entry_function.get()  # Lấy hàm người dùng nhập
        x = symbols('x')
        f = eval(func)  # Biểu thức hàm người dùng nhập
        integral = integrate(f, x)
        result_integral.set(f"Tích phân: {integral}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")


# Hàm vẽ đồ thị hàm số
def plot_graph():
    try:
        func = entry_function.get()  # Lấy hàm người dùng nhập
        x = symbols('x')
        f = eval(func)  # Biểu thức hàm người dùng nhập

        # Vẽ đồ thị
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [f.subs(x, val) for val in x_vals]

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='Hàm số', color='blue')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f"Đồ thị của hàm: {func}")
        ax.legend()

        # Đưa đồ thị vào trong cửa sổ Tkinter
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=4)
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")


# Hàm giải phương trình
def solve_equation():
    try:
        eq_str = entry_equation.get()  # Nhập phương trình từ người dùng
        x = symbols('x')
        eq = Eq(eval(eq_str), 0)  # Biểu thức phương trình
        solutions = solve(eq, x)
        result_equation.set(f"Nghiệm phương trình: {solutions}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")


# Giao diện người dùng (UI)
label_function = tk.Label(root, text="Nhập hàm f(x):")
label_function.grid(row=0, column=0, padx=10, pady=10)
entry_function = tk.Entry(root)
entry_function.grid(row=0, column=1, padx=10, pady=10)

label_equation = tk.Label(root, text="Nhập phương trình (Ví dụ: x**2 - 4):")
label_equation.grid(row=1, column=0, padx=10, pady=10)
entry_equation = tk.Entry(root)
entry_equation.grid(row=1, column=1, padx=10, pady=10)

# Nút tính đạo hàm
button_derivative = tk.Button(root, text="Tính đạo hàm", command=calculate_derivative)
button_derivative.grid(row=2, column=0, padx=10, pady=10)

# Nút tính tích phân
button_integral = tk.Button(root, text="Tính tích phân", command=calculate_integral)
button_integral.grid(row=2, column=1, padx=10, pady=10)

# Nút vẽ đồ thị
button_plot = tk.Button(root, text="Vẽ đồ thị", command=plot_graph)
button_plot.grid(row=2, column=2, padx=10, pady=10)

# Nút giải phương trình
button_solve = tk.Button(root, text="Giải phương trình", command=solve_equation)
button_solve.grid(row=3, column=0, padx=10, pady=10)

# Kết quả
result_derivative = tk.StringVar()
result_integral = tk.StringVar()
result_equation = tk.StringVar()

label_result_derivative = tk.Label(root, textvariable=result_derivative)
label_result_derivative.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

label_result_integral = tk.Label(root, textvariable=result_integral)
label_result_integral.grid(row=4, column=3, padx=10, pady=5)

label_result_equation = tk.Label(root, textvariable=result_equation)
label_result_equation.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

# Khởi chạy giao diện
root.mainloop()
