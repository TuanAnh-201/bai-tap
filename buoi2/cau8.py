import cv2
import numpy as np

def apply_gaussian_filter(image, kernel_size, sigma):
    # Tạo kernel Gaussian
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = kernel * kernel.T

    # Áp dụng lọc
    dst = cv2.filter2D(image, -1, kernel)
    return dst

# Đọc ảnh
img = cv2.imread('image.jpg')

# Lọc ảnh
filtered_img = apply_gaussian_filter(img, 5, 1.5)

# Hiển thị ảnh
cv2.imshow('Original', img)
cv2.imshow('Filtered', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()