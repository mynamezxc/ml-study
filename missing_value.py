# Điền vào những record empty data
from sklearn.impute import SimpleImputer
import pandas
import numpy as np

data = pandas.read_csv("./csv/missing.csv", header=1, error_bad_lines=False)
print(data)

data = data.values
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent') # mean là lấy trung bình của cột, most_frequent để lấy cái sử dụng nhiều nhất của cột
imputer.fit(data)
result = imputer.transform(data)
print(result)