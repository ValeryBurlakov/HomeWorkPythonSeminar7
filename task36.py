from datetime import datetime
import time

time_01 = datetime.now()
def print_operation_table_3(operation, num_rows=100, num_columns=100000):   
    for i in range(1, num_rows + 1): (print('\t'.join(str(operation(i, j))for j in range(1, num_columns + 1))))
    # for i in range(1, num_rows + 1):
    #     print ('\t'.join(str(operation(i, j)) for j in range(1, num_columns + 1)))
print_operation_table_3(lambda x, y: x * y) 
time_1 = datetime.now() - time_01


time_02 = datetime.now()
def print_operation_table_2(operation, num_rows=100, num_columns=100000):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            nums.append(num)
        print('\t'.join([str(x) for x in nums]))
print_operation_table_2(lambda x, y: x * y) 
time_2 = datetime.now() - time_02

# num_rows = int() # ЧЕРНОВИК
# num_columns = int() # ЧЕРНОВИК

# def operation(x,y): # ЧЕРНОВИК
#     return lambda x, y: x * y

time_03 = datetime.now()
def print_operation_table(operation, num_rows=100, num_columns=100000):
    for rows_index in range(1, num_rows + 1):
        for columns_index in range(1, num_columns + 1):
            print(operation(rows_index, columns_index), end="\t")
        print()
print_operation_table(lambda x, y: x * y)
time_3 = datetime.now() - time_03

# print_operation_table(operation(num_rows, num_columns)) # ЧЕРНОВИК
print(time_1)
print(time_2)
print(time_3)