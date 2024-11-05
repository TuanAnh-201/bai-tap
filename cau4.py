import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


# Hàm tính toán chỉ số hiệu suất và tạo báo cáo cho từng học sinh
def generate_report():
    # Kiểm tra xem có dữ liệu trong DataFrame hay không
    if df is None:
        messagebox.showerror("Lỗi", "Vui lòng tải file CSV trước.")
        return

    # Tạo báo cáo cho từng học sinh
    report_text = "Báo cáo học phần:\n\n"

    for _, row in df.iterrows():
        study_hours = row['Giờ học']
        previous_scores = row['Điểm số trước']
        extracurricular_hours = row['Hoạt động ngoại khóa']
        sleep_hours = row['Giờ ngủ']
        homework_completion = row['Hoàn thành bài tập mẫu câu hỏi']

        # Tính toán chỉ số hiệu suất học tập
        performance_index = (study_hours * 0.3) + (previous_scores * 0.3) + (extracurricular_hours * 0.2) + (
                    sleep_hours * 0.1) + (homework_completion * 0.1)
        performance_index = np.clip(performance_index, 0, 10)

        # Cập nhật báo cáo
        report_text += f"Tên: {row['Tên']} {row['Họ']}\n"
        report_text += f"Giờ học: {study_hours} giờ\n"
        report_text += f"Điểm số trước đó: {previous_scores}\n"
        report_text += f"Hoạt động ngoại khóa: {extracurricular_hours} giờ\n"
        report_text += f"Giờ ngủ: {sleep_hours} giờ\n"
        report_text += f"Hoàn thành bài tập mẫu: {homework_completion}\n"
        report_text += f"Chỉ số hiệu suất: {performance_index:.2f}\n\n"

    # Hiển thị báo cáo
    report.set(report_text)

    # Vẽ đồ thị hiệu suất học tập của các học sinh
    plot_performance()


# Hàm vẽ đồ thị phân tích các yếu tố ảnh hưởng đến hiệu suất học tập
def plot_performance():
    if df is None:
        return

    # Vẽ đồ thị các yếu tố ảnh hưởng đến hiệu suất học tập
    study_hours = df['Giờ học']
    previous_scores = df['Điểm số trước']
    extracurricular_hours = df['Hoạt động ngoại khóa']
    sleep_hours = df['Giờ ngủ']
    homework_completion = df['Hoàn thành bài tập mẫu câu hỏi']

    # Tính toán chỉ số hiệu suất
    performance_index = (study_hours * 0.3) + (previous_scores * 0.3) + (extracurricular_hours * 0.2) + (
                sleep_hours * 0.1) + (homework_completion * 0.1)
    performance_index = np.clip(performance_index, 0, 10)

    # Vẽ biểu đồ
    fig, ax = plt.subplots()
    ax.bar(df['Tên'], performance_index, color='skyblue')
    ax.set_title('Chỉ số hiệu suất học tập của các học sinh')
    ax.set_ylabel('Chỉ số hiệu suất')

    # Đưa đồ thị vào trong cửa sổ Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=4)
    canvas.draw()


# Hàm tải file CSV và đọc dữ liệu vào DataFrame
def load_csv():
    global df
    # Mở hộp thoại để chọn file CSV
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        # Đọc dữ liệu từ file CSV vào DataFrame
        df = pd.read_csv(file_path)
        if not all(col in df.columns for col in
                   ['Tên', 'Họ', 'Giờ học', 'Điểm số trước', 'Hoạt động ngoại khóa', 'Giờ ngủ',
                    'Hoàn thành bài tập mẫu câu hỏi']):
            messagebox.showerror("Lỗi", "File CSV không có đủ các cột yêu cầu.")
            df = None
            return
        messagebox.showinfo("Thông báo", "Dữ liệu đã được tải thành công.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải file CSV: {e}")
        df = None


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

# Kết quả báo cáo
report = tk.StringVar()

label_result_report = tk.Label(root, textvariable=report, justify=tk.LEFT, anchor="w", width=50, height=15)
label_result_report.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Khởi chạy giao diện
root.mainloop()
