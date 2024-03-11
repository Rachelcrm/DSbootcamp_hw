import pandas as pd
import numpy as np
#1
def MMT():
    read_file = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    filtered_file = read_file.iloc[::20, :][['Manufacturer', 'Model', 'Type']]
    print(filtered_file)

#2
def replace_missing():
    read_file = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
    read_file['Min.Price'] = read_file['Min.Price'].fillna(read_file['Min.Price'].mean())
    read_file['Max.Price'] = read_file['Max.Price'].fillna(read_file['Max.Price'].mean())
    print(read_file[['Min.Price', 'Max.Price']])

#3
def rows_with_sum_greater_than_100():
    read_file = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
    filtered_file = read_file[read_file.sum(axis=1) > 100]
    print(filtered_file)

#4
def create_array():
    new_array = np.random.randint(1, 101, size=(4, 4))
    row_array = new_array.reshape(2, 8)
    col_array = new_array.T.reshape(2, 8)
    sum_row = lambda arr: np.array([np.sum(row) for row in arr])
    sum_col = lambda arr: np.array([np.sum(col) for col in arr])
    sum_of_rows = sum_row(row_array)
    sum_of_columns = sum_col(col_array)
    print("Sum of each row:", sum_of_rows)
    print("Sum of each column:", sum_of_columns)