import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.fft import fft, ifft
from scipy.signal import butter, lfilter


# Hàm tạo tín hiệu dạng sóng sin
def create_signal(frequency=5, sampling_rate=100, duration=1):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal


# Hàm thực hiện biến đổi Fourier (FFT)
def compute_fft(signal, sampling_rate=100):
    N = len(signal)
    freq = np.fft.fftfreq(N, d=1 / sampling_rate)
    fft_signal = fft(signal)
    return freq, fft_signal


# Hàm lọc FIR (Bộ lọc cửa sổ)
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def apply_lowpass_filter(signal, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order)
    return lfilter(b, a, signal)


# Hàm vẽ tín hiệu trong miền thời gian
def plot_time_domain(t, signal, title="Tín hiệu trong miền thời gian"):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(t, signal)
    ax.set_title(title)
    ax.set_xlabel('Thời gian (s)')
    ax.set_ylabel('Biên độ')
    ax.grid(True)

    # Hiển thị đồ thị trong giao diện Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, padx=10, pady=10)
    canvas.draw()


# Hàm vẽ tín hiệu trong miền tần số
def plot_frequency_domain(freq, fft_signal, title="Biến đổi Fourier"):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(freq, np.abs(fft_signal))
    ax.set_title(title)
    ax.set_xlabel('Tần số (Hz)')
    ax.set_ylabel('Biên độ')
    ax.grid(True)

    # Hiển thị đồ thị trong giao diện Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=4, padx=10, pady=10)
    canvas.draw()


# Hàm xử lý tín hiệu theo yêu cầu của người dùng
def process_signal():
    frequency = float(entry_freq.get())
    sampling_rate = int(entry_sampling_rate.get())
    duration = float(entry_duration.get())

    # Tạo tín hiệu sin
    t, signal = create_signal(frequency, sampling_rate, duration)

    # Vẽ tín hiệu trong miền thời gian
    plot_time_domain(t, signal, title="Tín hiệu trong miền thời gian")

    # Tính và vẽ Biến đổi Fourier (FFT)
    freq, fft_signal = compute_fft(signal, sampling_rate)
    plot_frequency_domain(freq, fft_signal, title="Biến đổi Fourier")

    # Nếu chọn lọc tín hiệu
    if var_lowpass.get():
        cutoff = float(entry_cutoff.get())
        filtered_signal = apply_lowpass_filter(signal, cutoff, sampling_rate)
        plot_time_domain(t, filtered_signal, title="Tín hiệu sau khi lọc")


# Giao diện phần mềm với Tkinter
root = tk.Tk()
root.title("Phần mềm hỗ trợ môn học Xử lý Tín hiệu Số")

# Cấu hình khung nhập liệu
frame_input = tk.Frame(root)
frame_input.grid(row=0, column=0, padx=10, pady=10)

# Tạo các trường nhập liệu
label_freq = tk.Label(frame_input, text="Tần số tín hiệu (Hz):")
label_freq.grid(row=0, column=0)
entry_freq = tk.Entry(frame_input)
entry_freq.grid(row=0, column=1)
entry_freq.insert(0, "5")  # Giá trị mặc định

label_sampling_rate = tk.Label(frame_input, text="Tần số mẫu (Hz):")
label_sampling_rate.grid(row=1, column=0)
entry_sampling_rate = tk.Entry(frame_input)
entry_sampling_rate.grid(row=1, column=1)
entry_sampling_rate.insert(0, "100")  # Giá trị mặc định

label_duration = tk.Label(frame_input, text="Thời gian (s):")
label_duration.grid(row=2, column=0)
entry_duration = tk.Entry(frame_input)
entry_duration.grid(row=2, column=1)
entry_duration.insert(0, "1")  # Giá trị mặc định

# Cấu hình lọc tín hiệu
var_lowpass = tk.BooleanVar()
var_lowpass.set(False)

checkbox_lowpass = tk.Checkbutton(frame_input, text="Lọc tín hiệu (Lowpass)", variable=var_lowpass)
checkbox_lowpass.grid(row=3, column=0, columnspan=2)

label_cutoff = tk.Label(frame_input, text="Tần số cắt (Hz):")
label_cutoff.grid(row=4, column=0)
entry_cutoff = tk.Entry(frame_input)
entry_cutoff.grid(row=4, column=1)
entry_cutoff.insert(0, "10")  # Giá trị mặc định

# Nút xử lý tín hiệu
button_process = tk.Button(root, text="Xử lý tín hiệu", command=process_signal)
button_process.grid(row=1, column=0, columnspan=4, pady=10)

# Chạy giao diện Tkinter
root.mainloop()
