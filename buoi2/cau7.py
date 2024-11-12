import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import tkinter as tk
from tkinter import messagebox
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('water_potability.csv')

# Xử lý dữ liệu thiếu: Điền giá trị thiếu bằng giá trị trung bình của cột
df.fillna(df.mean(), inplace=True)

# Chia dữ liệu thành đặc trưng (X) và nhãn (y)
X = df.drop('Potability', axis=1)  # Cột Potability là nhãn
y = df['Potability']

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu (Standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Tạo mô hình RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Đánh giá mô hình
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Vẽ confusion matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

# Hàm để dự đoán chất lượng nước
def predict_water_quality():
    try:
        # Lấy giá trị đầu vào từ các ô nhập
        ph = float(entry_ph.get())
        hardness = float(entry_hardness.get())
        solid = float(entry_solid.get())
        chloramines = float(entry_chloramines.get())
        sulfate = float(entry_sulfate.get())
        conductivity = float(entry_conductivity.get())
        organic_carbon = float(entry_organic_carbon.get())
        trihalomethanes = float(entry_trihalomethanes.get())
        turbidity = float(entry_turbidity.get())

        # Tạo mảng đặc trưng từ các giá trị đầu vào
        input_data = [[ph, hardness, solid, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]

        # Chuẩn hóa dữ liệu đầu vào
        input_data_scaled = scaler.transform(input_data)

        # Dự đoán chất lượng nước (Potability)
        prediction = model.predict(input_data_scaled)

        # Hiển thị kết quả
        if prediction == 1:
            messagebox.showinfo("Kết quả", "Nước có thể uống được (Potable).")
        else:
            messagebox.showwarning("Kết quả", "Nước không thể uống được (Non-potable).")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập các giá trị hợp lệ.")

# Tạo cửa sổ chính của giao diện người dùng
root = tk.Tk()
root.title("Ứng Dụng Xác Định Chất Lượng Nước")

# Tạo các nhãn và ô nhập liệu
tk.Label(root, text="pH").grid(row=0, column=0)
entry_ph = tk.Entry(root)
entry_ph.grid(row=0, column=1)

tk.Label(root, text="Hardness").grid(row=1, column=0)
entry_hardness = tk.Entry(root)
entry_hardness.grid(row=1, column=1)

tk.Label(root, text="Solid").grid(row=2, column=0)
entry_solid = tk.Entry(root)
entry_solid.grid(row=2, column=1)

tk.Label(root, text="Chloramines").grid(row=3, column=0)
entry_chloramines = tk.Entry(root)
entry_chloramines.grid(row=3, column=1)

tk.Label(root, text="Sulfate").grid(row=4, column=0)
entry_sulfate = tk.Entry(root)
entry_sulfate.grid(row=4, column=1)

tk.Label(root, text="Conductivity").grid(row=5, column=0)
entry_conductivity = tk.Entry(root)
entry_conductivity.grid(row=5, column=1)

tk.Label(root, text="Organic Carbon").grid(row=6, column=0)
entry_organic_carbon = tk.Entry(root)
entry_organic_carbon.grid(row=6, column=1)

tk.Label(root, text="Trihalomethanes").grid(row=7, column=0)
entry_trihalomethanes = tk.Entry(root)
entry_trihalomethanes.grid(row=7, column=1)

tk.Label(root, text="Turbidity").grid(row=8, column=0)
entry_turbidity = tk.Entry(root)
entry_turbidity.grid(row=8, column=1)

# Nút để dự đoán chất lượng nước
predict_button = tk.Button(root, text="Dự Đoán", command=predict_water_quality)
predict_button.grid(row=9, columnspan=2)

# Chạy ứng dụng Tkinter
root.mainloop()
