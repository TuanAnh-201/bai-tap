import cv2
import numpy as np

# Hàm áp dụng bộ lọc làm mịn
def apply_filter(frame, filter_type, kernel_size):
    if filter_type == 'Gaussian':
        return cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)
    elif filter_type == 'Median':
        return cv2.medianBlur(frame, kernel_size)
    elif filter_type == 'Bilateral':
        return cv2.bilateralFilter(frame, 9, 75, 75)
    else:
        return frame

# Khởi tạo camera (sử dụng camera mặc định của máy tính)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở camera!")
    exit()

# Tạo cửa sổ hiển thị
cv2.namedWindow("Camera Feed")

# Đặt các tham số lọc mặc định
filter_type = 'Gaussian'  # Mặc định là Gaussian
kernel_size = 5  # Kích thước bộ lọc mặc định
camera_active = True  # Biến kiểm tra trạng thái camera

# Vòng lặp chính của ứng dụng
while True:
    if camera_active:
        # Đọc một khung hình từ camera
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc khung hình từ camera!")
            break

        # Áp dụng bộ lọc làm mịn
        frame_filtered = apply_filter(frame, filter_type, kernel_size)

        # Hiển thị khung hình gốc và khung hình đã xử lý
        cv2.imshow('Original', frame)  # Hiển thị ảnh gốc
        cv2.imshow('Filtered', frame_filtered)  # Hiển thị ảnh sau khi lọc

    # Chờ người dùng nhấn phím để thay đổi bộ lọc hoặc thoát
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Nhấn 'q' để thoát
        break
    elif key == ord('g'):  # Nhấn 'g' để chọn Gaussian Blur
        filter_type = 'Gaussian'
    elif key == ord('m'):  # Nhấn 'm' để chọn Median Filter
        filter_type = 'Median'
    elif key == ord('b'):  # Nhấn 'b' để chọn Bilateral Filter
        filter_type = 'Bilateral'
    elif key == ord('r'):  # Nhấn 'r' để điều chỉnh kích thước bộ lọc
        kernel_size += 2
        if kernel_size > 21:  # Giới hạn kích thước bộ lọc (kích thước phải là số lẻ)
            kernel_size = 3
    elif key == ord('t'):  # Nhấn 't' để tắt camera
        if camera_active:
            print("Tắt camera...")
            camera_active = False
            cap.release()  # Giải phóng tài nguyên của camera
            cv2.destroyAllWindows()  # Đóng tất cả cửa sổ
        else:
            print("Mở lại camera...")
            cap = cv2.VideoCapture(0)  # Mở lại camera
            camera_active = True  # Kích hoạt lại camera

# Giải phóng camera và đóng tất cả cửa sổ khi thoát
if camera_active:
    cap.release()
cv2.destroyAllWindows()
