import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Phần mềm Hỗ trợ học tập môn Hình Học")

# Hàm tính diện tích và chu vi hình tròn
def calculate_circle():
    try:
        radius = float(entry_radius.get())  # Lấy bán kính từ người dùng
        area = math.pi * radius**2
        perimeter = 2 * math.pi * radius
        result_circle.set(f"Diện tích: {area:.2f}, Chu vi: {perimeter:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ cho bán kính.")

# Hàm tính diện tích và chu vi hình vuông
def calculate_square():
    try:
        side = float(entry_side.get())  # Lấy cạnh từ người dùng
        area = side**2
        perimeter = 4 * side
        result_square.set(f"Diện tích: {area:.2f}, Chu vi: {perimeter:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ cho cạnh.")

# Hàm tính diện tích và chu vi hình chữ nhật
def calculate_rectangle():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        area = length * width
        perimeter = 2 * (length + width)
        result_rectangle.set(f"Diện tích: {area:.2f}, Chu vi: {perimeter:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ cho chiều dài và chiều rộng.")

# Hàm tính thể tích hình hộp chữ nhật
def calculate_cuboid():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        height = float(entry_height.get())
        volume = length * width * height
        surface_area = 2 * (length*width + length*height + width*height)
        result_cuboid.set(f"Thể tích: {volume:.2f}, Diện tích xung quanh: {surface_area:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ cho chiều dài, chiều rộng và chiều cao.")

# Hàm vẽ hình tròn
def plot_circle():
    try:
        radius = float(entry_radius.get())  # Lấy bán kính từ người dùng
        fig, ax = plt.subplots()
        ax.set_xlim([-radius-1, radius+1])
        ax.set_ylim([-radius-1, radius+1])
        ax.set_aspect('equal')
        circle = plt.Circle((0, 0), radius, edgecolor='blue', facecolor='none')
        ax.add_artist(circle)
        ax.set_title(f"Hình tròn bán kính {radius}")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=3)
        canvas.draw()
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ cho bán kính.")

# Giao diện người dùng (UI)
label_radius = tk.Label(root, text="Nhập bán kính hình tròn:")
label_radius.grid(row=0, column=0, padx=10, pady=10)
entry_radius = tk.Entry(root)
entry_radius.grid(row=0, column=1, padx=10, pady=10)

label_side = tk.Label(root, text="Nhập cạnh hình vuông:")
label_side.grid(row=1, column=0, padx=10, pady=10)
entry_side = tk.Entry(root)
entry_side.grid(row=1, column=1, padx=10, pady=10)

label_length = tk.Label(root, text="Nhập chiều dài hình chữ nhật:")
label_length.grid(row=2, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=2, column=1, padx=10, pady=10)

label_width = tk.Label(root, text="Nhập chiều rộng hình chữ nhật:")
label_width.grid(row=3, column=0, padx=10, pady=10)
entry_width = tk.Entry(root)
entry_width.grid(row=3, column=1, padx=10, pady=10)

label_height = tk.Label(root, text="Nhập chiều cao hình hộp chữ nhật:")
label_height.grid(row=4, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=4, column=1, padx=10, pady=10)

# Nút tính diện tích và chu vi hình tròn
button_circle = tk.Button(root, text="Tính hình tròn", command=calculate_circle)
button_circle.grid(row=0, column=2, padx=10, pady=10)

# Nút tính diện tích và chu vi hình vuông
button_square = tk.Button(root, text="Tính hình vuông", command=calculate_square)
button_square.grid(row=1, column=2, padx=10, pady=10)

# Nút tính diện tích và chu vi hình chữ nhật
button_rectangle = tk.Button(root, text="Tính hình chữ nhật", command=calculate_rectangle)
button_rectangle.grid(row=2, column=2, padx=10, pady=10)

# Nút tính thể tích hình hộp chữ nhật
button_cuboid = tk.Button(root, text="Tính hình hộp chữ nhật", command=calculate_cuboid)
button_cuboid.grid(row=3, column=2, padx=10, pady=10)

# Nút vẽ hình tròn
button_plot_circle = tk.Button(root, text="Vẽ hình tròn", command=plot_circle)
button_plot_circle.grid(row=4, column=2, padx=10, pady=10)

# Kết quả tính toán
result_circle = tk.StringVar()
result_square = tk.StringVar()
result_rectangle = tk.StringVar()
result_cuboid = tk.StringVar()

label_result_circle = tk.Label(root, textvariable=result_circle)
label_result_circle.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

label_result_square = tk.Label(root, textvariable=result_square)
label_result_square.grid(row=5, column=2, padx=10, pady=5)

label_result_rectangle = tk.Label(root, textvariable=result_rectangle)
label_result_rectangle.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

label_result_cuboid = tk.Label(root, textvariable=result_cuboid)
label_result_cuboid.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

# Khởi chạy giao diện
root.mainloop()
