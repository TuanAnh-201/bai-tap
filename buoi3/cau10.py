import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hàm tăng cường độ sáng
def increase_brightness(image, value=50):
    return cv2.convertScaleAbs(image, alpha=1, beta=value)

# Hàm điều chỉnh độ tương phản
def enhance_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    return cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

# Hàm giảm nhiễu bằng Gaussian Blur
def reduce_noise(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

# Hàm mở cửa sổ chọn tệp ảnh
def load_image():
    Tk().withdraw()  # Ẩn cửa sổ chính của Tkinter
    filename = askopenfilename(title="Chọn ảnh", filetypes=[("Image Files", "*.jfif *.jpg *.jpeg *.png *.bmp")])
    if filename:
        return cv2.imread(filename)
    else:
        print("Không có ảnh nào được chọn!")
        exit()

# Đọc ảnh từ file thông qua hộp thoại
image = load_image()

# Kiểm tra xem ảnh có được tải thành công không
if image is None:
    print("Không thể tải ảnh. Vui lòng kiểm tra lại tệp ảnh.")
    exit()

# Tăng độ sáng
image_bright = increase_brightness(image)

# Cải thiện độ tương phản
image_contrast = enhance_contrast(image_bright)







# Giảm nhiễu
image_enhanced = reduce_noise(image_contrast)

# Hiển thị ảnh gốc và ảnh đã xử lý
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Ảnh Gốc')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image_enhanced, cv2.COLOR_BGR2RGB))
plt.title('Ảnh Sau Khi Tăng Cường')
plt.axis('off')

plt.show()

# Lưu ảnh đã xử lý
output_path = 'image_enhanced.jpg'
cv2.imwrite(output_path, image_enhanced)
print(f"Ảnh đã được lưu tại {output_path}")
