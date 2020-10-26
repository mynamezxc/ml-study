import pandas

scv_data = pandas.read_csv("UNSW_NB15_training-set.csv", header=None)
print(scv_data)
# Viet collumn so 3 vao file new_file.csv
scv_data = scv_data[3] # [collumn][row]
scv_data.to_csv("new_file.csv")