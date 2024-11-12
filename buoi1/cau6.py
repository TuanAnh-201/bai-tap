import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Bước 1: Đọc dữ liệu từ file CSV
file_path = 'Student_Performance.csv'  # Đường dẫn tới file CSV
data = pd.read_csv(file_path)

# Hiển thị vài dòng đầu tiên của dữ liệu
print(data.head())

# Bước 2: Tiền xử lý dữ liệu
# Kiểm tra các giá trị thiếu (nếu có)
print(data.isnull().sum())

# Nếu có dữ liệu thiếu, chúng ta có thể xử lý bằng cách loại bỏ hoặc thay thế
data = data.dropna()  # Loại bỏ các dòng có giá trị thiếu

# Bước 3: Phân tích dữ liệu
# Vẽ biểu đồ tương quan giữa các biến
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Ma trận tương quan giữa các yếu tố")
plt.show()

# Bước 4: Xây dựng mô hình dự đoán
# Chọn các đặc trưng và biến mục tiêu
X = data[['Số giờ học', 'Điểm số trước', 'Hoạt động ngoại khóa', 'Giờ ngủ', 'Bài tập mẫu câu hỏi']]
y = data['Chỉ số hiệu suất']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra (train/test split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bước 5: Khởi tạo và huấn luyện mô hình Hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Bước 6: Dự đoán và đánh giá mô hình
y_pred = model.predict(X_test)

# Đánh giá độ chính xác của mô hình
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# In kết quả đánh giá
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R²): {r2}")

# Bước 7: Vẽ đồ thị so sánh kết quả dự đoán và giá trị thực tế
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2)
plt.xlabel('Giá trị thực tế')
plt.ylabel('Giá trị dự đoán')
plt.title('So sánh giá trị thực tế và dự đoán')
plt.show()
