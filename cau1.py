import tkinter as tk
from tkinter import messagebox
import numpy as np


# Hàm giải hệ phương trình tuyến tính
def solve_linear_system(A, B):
    try:
        # Kiểm tra tính khả nghịch của ma trận A
        det_A = np.linalg.det(A)
        if det_A == 0:
            messagebox.showerror("Lỗi",
                                 "Ma trận A không khả nghịch (det(A) = 0). Hệ phương trình không có nghiệm duy nhất.")
            return None

        # Tính ma trận nghịch đảo của A
        A_inv = np.linalg.inv(A)

        # Tính nghiệm của hệ phương trình
        X = np.dot(A_inv, B)
        return X

    except np.linalg.LinAlgError as e:
        # Nếu gặp lỗi trong quá trình tính toán (ví dụ: ma trận không vuông)
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")
        return None


# Hàm xử lý khi người dùng bấm nút "Giải"
def on_solve():
    try:
        # Lấy giá trị ma trận A từ các ô nhập liệu
        A11 = float(entry_A11.get())
        A12 = float(entry_A12.get())
        A21 = float(entry_A21.get())
        A22 = float(entry_A22.get())

        # Tạo ma trận A
        A = np.array([[A11, A12], [A21, A22]])

        # Lấy giá trị vector B từ các ô nhập liệu
        B1 = float(entry_B1.get())
        B2 = float(entry_B2.get())

        # Tạo vector B
        B = np.array([B1, B2])

        # Giải hệ phương trình
        X = solve_linear_system(A, B)

        if X is not None:
            # Hiển thị nghiệm vào các ô kết quả
            result_x.set(f"{X[0]:.2f}")
            result_y.set(f"{X[1]:.2f}")

    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập đúng số liệu cho ma trận và vector.")


# Tạo cửa sổ ứng dụng
root = tk.Tk()
root.title("Giải hệ phương trình tuyến tính A * X = B")

# Tạo các nhãn và ô nhập liệu cho ma trận A
label_A = tk.Label(root, text="Nhập ma trận A (2x2):")
label_A.grid(row=0, column=0, columnspan=2)

label_A11 = tk.Label(root, text="A[0,0]:")
label_A11.grid(row=1, column=0)
entry_A11 = tk.Entry(root)
entry_A11.grid(row=1, column=1)

label_A12 = tk.Label(root, text="A[0,1]:")
label_A12.grid(row=2, column=0)
entry_A12 = tk.Entry(root)
entry_A12.grid(row=2, column=1)

label_A21 = tk.Label(root, text="A[1,0]:")
label_A21.grid(row=3, column=0)
entry_A21 = tk.Entry(root)
entry_A21.grid(row=3, column=1)

label_A22 = tk.Label(root, text="A[1,1]:")
label_A22.grid(row=4, column=0)
entry_A22 = tk.Entry(root)
entry_A22.grid(row=4, column=1)

# Tạo các nhãn và ô nhập liệu cho vector B
label_B = tk.Label(root, text="Nhập vector B:")
label_B.grid(row=5, column=0, columnspan=2)

label_B1 = tk.Label(root, text="B[0]:")
label_B1.grid(row=6, column=0)
entry_B1 = tk.Entry(root)
entry_B1.grid(row=6, column=1)

label_B2 = tk.Label(root, text="B[1]:")
label_B2.grid(row=7, column=0)
entry_B2 = tk.Entry(root)
entry_B2.grid(row=7, column=1)

# Nút giải phương trình
solve_button = tk.Button(root, text="Giải", command=on_solve)
solve_button.grid(row=8, column=0, columnspan=2)

# Kết quả nghiệm X
label_result = tk.Label(root, text="Nghiệm của hệ:")
label_result.grid(row=9, column=0, columnspan=2)

result_x = tk.StringVar()
result_y = tk.StringVar()

label_x = tk.Label(root, text="X[0]:")
label_x.grid(row=10, column=0)
entry_x = tk.Entry(root, textvariable=result_x, state="readonly")
entry_x.grid(row=10, column=1)

label_y = tk.Label(root, text="X[1]:")
label_y.grid(row=11, column=0)
entry_y = tk.Entry(root, textvariable=result_y, state="readonly")
entry_y.grid(row=11, column=1)

# Khởi chạy giao diện
root.mainloop()
