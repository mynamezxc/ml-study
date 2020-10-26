from sklearn import tree
from matplotlib import pyplot
import numpy

# Tạo cây quyết định
tree = tree.DecisionTreeClassifier()
data = [
    [1,3,3,7],
    [5,2,4,6],
    [1,2,4,6],
    [5,4,4,3],
    [1,4,4,7],
    [3,2,3,7],
    [3,3,3,6],
    [5,2,2,7]
]
result_of_data = [0, 1, 1, 0, 0, 0, 0, 1]
fited = tree.fit(data, result_of_data)
response = fited.predict([[1, 2, 4, 7]])
print(response)