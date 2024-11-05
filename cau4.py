import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Hàm tính toán điểm cuối kỳ dựa trên các yếu tố
def calculate_final_score(row):
    # Lấy các điểm số từ các cột tương ứng
    L1 = row['L1']
    L2 = row['L2']
    TX1 = row['TX1']
    TX2 = row['TX2']

    # Tính điểm cuối kỳ (công thức có thể thay đổi theo yêu cầu)
    final_score = (L1 * 0.3) + (L2 * 0.3) + (TX1 * 0.2) + (TX2 * 0.2)
    return np.clip(final_score, 0, 10)


# Hàm tạo báo cáo
def generate_report():
    if df is None:
        messagebox.showerror("Lỗi", "Vui lòng tải file CSV trước.")
        return

    # Tính toán điểm cuối kỳ cho từng sinh viên và tạo báo cáo
    report_text = "Báo cáo học phần:\n\n"

    df['Cuối kỳ'] = df.apply(calculate_final_score, axis=1)

    for _, row in df.iterrows():
        report_text += f"Mã lớp: {row['Mã lớp']}\n"
        report_text += f"Số sinh viên: {row['Số SV']}\n"
        report_text += f"Loại A+: {row['Loại A+']}\n"
        report_text += f"Loại A: {row['Loại A']}\n"
        report_text += f"Loại B+: {row['Loại B+']}\n"
        report_text += f"Loại B: {row['Loại B']}\n"
        report_text += f"Loại C+: {row['Loại C+']}\n"
        report_text += f"Loại C: {row['Loại C']}\n"
        report_text += f"Loại D+: {row['Loại D+']}\n"
        report_text += f"Loại D: {row['Loại D']}\n"
        report_text += f"Loại F: {row['Loại F']}\n"
        report_text += f"Điểm L1: {row['L1']}\n"
        report_text += f"Điểm L2: {row['L2']}\n"
        report_text += f"Điểm TX1: {row['TX1']}\n"
        report_text += f"Điểm TX2: {row['TX2']}\n"
        report_text += f"Điểm cuối kỳ: {row['Cuối kỳ']:.2f}\n\n"

    # Cập nhật báo cáo lên giao diện
    report.set(report_text)

    # Vẽ đồ thị kết quả học tập
    plot_performance()


# Hàm vẽ đồ thị kết quả học tập của các lớp
def plot_performance():
    if df is None:
        return

    # Vẽ đồ thị kết quả cuối kỳ
    class_names = df['Mã lớp']
    final_scores = df['Cuối kỳ']

    # Vẽ biểu đồ
    fig, ax = plt.subplots()
    ax.bar(class_names, final_scores, color='skyblue')
    ax.set_title('Kết quả cuối kỳ của các lớp')
    ax.set_ylabel('Điểm cuối kỳ')
    ax.set_xticklabels(class_names, rotation=45, ha='right')

    # Đưa đồ thị vào trong cửa sổ Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=4)
    canvas.draw()


# Hàm tải file CSV
def load_csv():
    global df
    # Mở hộp thoại để chọn file CSV
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        # Đọc dữ liệu từ file CSV vào DataFrame
        df = pd.read_csv(file_path)

        # Kiểm tra xem các cột dữ liệu có hợp lệ hay không
        required_columns = ['STT', 'Mã lớp', 'Số SV', 'Loại A+', 'Loại A', 'Loại B+', 'Loại B', 'Loại C+', 'Loại C',
                            'Loại D+', 'Loại D', 'Loại F', 'L1', 'L2', 'TX1', 'TX2', 'Cuối kỳ']
        if not all(col in df.columns for col in required_columns):
            messagebox.showerror("Lỗi", "File CSV không có đủ các cột yêu cầu.")
            df = None
            return

        messagebox.showinfo("Thông báo", "Dữ liệu đã được tải thành công.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải file CSV: {e}")
        df = None


# Hàm lưu báo cáo ra file CSV mới
def save_report():
    if df is None:
        messagebox.showerror("Lỗi", "Không có dữ liệu để lưu báo cáo.")
        return

    try:
        # Lưu DataFrame vào một file CSV mới
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Thông báo", "Báo cáo đã được lưu thành công.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu báo cáo: {e}")


# Khởi tạo DataFrame là None
df = None

# Giao diện người dùng (UI)
root = tk.Tk()
root.title("Chương trình tạo báo cáo học phần môn học")

# Nút tải file CSV
button_load_csv = tk.Button(root, text="Tải File CSV", command=load_csv)
button_load_csv.grid(row=0, column=0, padx=10, pady=10)

# Nút tạo báo cáo
button_generate_report = tk.Button(root, text="Tạo Báo Cáo", command=generate_report)
button_generate_report.grid(row=1, column=0, padx=10, pady=10)

# Nút lưu báo cáo
button_save_report = tk.Button(root, text="Lưu Báo Cáo", command=save_report)
button_save_report.grid(row=1, column=1, padx=10, pady=10)

# Kết quả báo cáo
report = tk.StringVar()

label_result_report = tk.Label(root, textvariable=report, justify=tk.LEFT, anchor="w", width=50, height=15)
label_result_report.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Khởi chạy giao diện
root.mainloop()
