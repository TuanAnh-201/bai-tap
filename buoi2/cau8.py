import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


# Hàm xử lý ảnh
def apply_filter():
    global img, photo

    # Lấy giá trị từ thanh trượt
    kernel_size = slider.get()

    # Chọn bộ lọc Gaussian Blur
    if filter_type.get() == "Gaussian":
        filtered_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    # Chọn bộ lọc Median Filter
    elif filter_type.get() == "Median":
        filtered_img = cv2.medianBlur(img, kernel_size)

    # Chọn bộ lọc Bilateral Filter
    elif filter_type.get() == "Bilateral":
        filtered_img = cv2.bilateralFilter(img, 9, 75, 75)

    # Chuyển ảnh đã xử lý thành dạng có thể hiển thị trên Tkinter
    filtered_img_rgb = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(filtered_img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Cập nhật ảnh trong giao diện
    panel.config(image=img_tk)
    panel.image = img_tk


# Hàm tải ảnh
def load_image():
    global img, photo

    # Chọn file ảnh
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Đọc ảnh và chuyển đổi màu sắc
    img = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Chuyển ảnh từ mảng NumPy sang hình ảnh có thể hiển thị
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Hiển thị ảnh lên giao diện
    panel.config(image=img_tk)
    panel.image = img_tk


# Khởi tạo giao diện người dùng (GUI) bằng Tkinter
root = Tk()
root.title("Ứng Dụng Lọc Làm Mịn Ảnh")

# Panel để hiển thị ảnh
panel = Label(root)
panel.pack(padx=10, pady=10)

# Nút tải ảnh
btn_load = Button(root, text="Tải ảnh", command=load_image)
btn_load.pack(padx=10, pady=10)

# Chọn bộ lọc
filter_type = StringVar(value="Gaussian")
filter_menu = OptionMenu(root, filter_type, "Gaussian", "Median", "Bilateral")
filter_menu.pack(padx=10, pady=10)

# Thanh trượt điều chỉnh kích thước bộ lọc
slider = Scale(root, from_=3, to_=21, orient=HORIZONTAL, label="Kích thước bộ lọc", resolution=2)
slider.set(5)  # Đặt giá trị mặc định cho thanh trượt
slider.pack(padx=10, pady=10)

# Nút áp dụng bộ lọc
btn_apply = Button(root, text="Áp dụng bộ lọc", command=apply_filter)
btn_apply.pack(padx=10, pady=10)

# Khởi động giao diện
root.mainloop()
