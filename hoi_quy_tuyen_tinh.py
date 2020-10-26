# https://www.youtube.com/watch?v=_x1ncKk8rgc&list=PLZEIt444jqpBPoqtW2ARJp9ICnF3c7vJC&index=11
# y = mx + b
# Tỉ lệ giá vốn/giá bán > Vốn để sales
# 31.5 | 12.2
# 25.8 | 8.4
# 72.5 | 56.1
# 45.1 | ???
# => Tỉ lệ vốn/giá bán X là số độc lập biết trước (giá trị không phụ thuộc biến khác), ml gọi là features
# => m là hệ số của biến độc lập X, ml gọi là weight
# => Bias là b là giá trị lệch để bù vào sai số của phương trình
# => y là biến phụ thuọc
# MSE là hàm lỗi, đo sự sai số bằng cách lấy trung bình bình phương giữa giá trị dự đoán và giá trị thực tế.
# => Tối thiểu MSE để tăng độ chính xác
# Learning rate là tốc độ học (bước nhảu của độ sai số)
# Công thức tính sai số Lấy weight và bias hiện tại (set mặc định) - ((Trung bình tổng bình phương của giá trị thực - giá trị dự đoán) * learning_rate)