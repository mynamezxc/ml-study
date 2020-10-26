from sklearn.tree import DecisionTreeClassifier
import numpy
import pandas
from matplotlib import pyplot
from sklearn.impute import SimpleImputer


def predict(x, weight, bias): # Hàm dự đoán
    return weight * x + bias


def cost_calcualation(x, y, weight, bias): # Tính tổng lỗi
    n = len(x)
    total_error = 0
    for i in range(n):
        total_error += (y[i] - (weight * x[i] + bias))**2 # bình phương của giá trị thực - giá trị dự đoán
    total_error = total_error / n # Trung bình tổng
    return total_error


def update_weight(x, y, weight, bias, learning_rate):
    n = len(x)
    weight_temp = 0.0
    bias_temp = 0.0
    for i in range(n):
        # Tính đạo hàm của weight = -2*x[i] * (giá trị thực - giá trị dự đoán)
        weight_temp += -2 * x[i] * (y[i] - (x[i] * weight + bias))
        # Tính đạo hàm của bias = -2 * (giá trị thực - giá trị dự đoán)
        bias_temp += -2 * (y[i] - (x[i] * weight + bias))
    # Tính trung bình của weight, bias
    # Công thức cho weight hoặc bias = a:  a = a - (trung bình tổng) * learning_rate
    weight -= (weight_temp/n) * learning_rate
    bias -= (bias_temp/n) * learning_rate
    return weight, bias


def training(x, y, weight, bias, learning_rate, interval):
    cost_histories = []
    for i in range(interval):
        weight, bias = update_weight(x, y, weight, bias, learning_rate)
        cost = cost_calcualation(x, y, weight, bias)
        cost_histories.append(cost)
    return weight, bias, cost_histories


dataframe = pandas.read_csv("./csv/Advertising.csv", header=1)
x = dataframe.values[:, 2] # Get data train ở cột số 3
y = dataframe.values[:, 4] # Get
pyplot.scatter(x, y, marker="o")
pyplot.show()

interval = 5000 # Số lần tối ưu
weight = 0.03 # Hệ số của x
bias = 0.014 # Giá trị lệch mặc định
learning_rate = 0.001 # Tốc độ học, bước học
weight, bias, cost_history = training(x, y, 0.03, 0.014, learning_rate, interval)

rating = 7
sales = rating * weight + bias
print("Kết quả: ")
print(sales)

# In ra các sai số theo số lần lặp, sai số sẽ nhỏ lại
loop = [i for i in range(interval)]
pyplot.plot(loop, cost_history)
pyplot.show()