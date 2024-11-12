import cv2
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt


# Hàm để mở cửa sổ chọn file và thực hiện tách biên ảnh
def open_image_and_edge_detection():
    # Mở cửa sổ chọn file ảnh
    file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.jpg; *.jfif;*.jpeg;*.png;*.bmp")])

    if not file_path:
        print("Không có tệp ảnh được chọn.")
        return

    # Đọc ảnh từ file
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    # Kiểm tra ảnh có được đọc thành công không
    if image is None:
        print(f"Không thể mở ảnh: {file_path}")
        return

    # Áp dụng Gaussian Blur để giảm nhiễu
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Áp dụng Canny Edge Detection
    edges = cv2.Canny(blurred_image, 100, 200)

    # Hiển thị ảnh gốc và ảnh tách biên
    plt.figure(figsize=(10, 5))

    # Hiển thị ảnh gốc
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Ảnh Gốc')
    plt.axis('off')

    # Hiển thị ảnh tách biên
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Ảnh Tách Biên (Canny)')
    plt.axis('off')

    # Hiển thị hình ảnh
    plt.show()


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Tách Biên Ảnh")

# Tạo nút để mở cửa sổ chọn ảnh và thực hiện tách biên
button = tk.Button(root, text="Chọn ảnh và tách biên", command=open_image_and_edge_detection)
button.pack(pady=20)

# Chạy giao diện Tkinter
root.mainloop()
