from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris # Tạo datasets
from sklearn.model_selection import train_test_split # train_test_split dùng tạo data để train từ datasets 75% để train, 25% để test
import numpy as np

dataset = load_iris()
x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, random_state=0) # Random_state=1 để lấy random mỗi lần chạy
# X là data, y là nhãn của mỗi dòng x
model = DecisionTreeClassifier()
myModel = model.fit(x_train, y_train)

print(myModel.predict(x_test))
print(y_test)
# Kiểm tra độ sai chính xác của nhãn test so với dòng test
print("Tỉ lệ chính xác: " + str(model.score(x_test, y_test)))