from sklearn import tree
from matplotlib import pyplot
import numpy

# Vẽ đồ thị, biểu đồ
#1
# x = [3, 7, 9, 12, 15, 4, 6]
# y = [2, 12, 8, 4, 19, 2, 12]
# pyplot.plot(x, y)
# pyplot.show()
#2
image = numpy.random.rand(10, 10)# Tạo mảng 2 chiều 30 x 30 random giá trị 0 -> 0.9999
# print(image)
pyplot.imshow(image) # Tạo 1 màu cho mỗi giá trị trong mảng, giống nhau thì cùng màu
pyplot.show()