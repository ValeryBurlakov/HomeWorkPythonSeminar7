# Без записи в таблицу
def print_operation_table(operation, num_rows=6, num_columns=6):   
    # for i in range(1, num_rows + 1): (print('\t'.join(str(operation(i, j))for j in range(1, num_columns + 1))))
    for i in range(1, num_rows + 1):
        print ('\t'.join(str(operation(i, j)) for j in range(1, num_columns + 1)))

print_operation_table(lambda x, y: x * y) 




# С записью в таблицу
# def print_operation_table_2(operation, num_rows=6, num_columns=6):
#     for x in range(1, num_rows + 1):
#         nums = []
#         for y in range(1, num_columns + 1):
#             num = operation(x, y)
#             nums.append(num)
#         print('\t'.join([str(x) for x in nums]))
        
# print_operation_table_2(lambda x, y: x * y) 




# Черновик
# num_rows = int() # ЧЕРНОВИК
# num_columns = int() # ЧЕРНОВИК

# def operation(x,y): # ЧЕРНОВИК
#     return lambda x, y: x * y

# def print_operation_table_3(operation, num_rows=6, num_columns=6):
#     for rows_index in range(1, num_rows + 1):
#         for columns_index in range(1, num_columns + 1):
#             print(operation(rows_index, columns_index), end="\t")
#         print()

# print_operation_table_3(lambda x, y: x * y)

# print_operation_table_3(operation(num_rows, num_columns)) # ЧЕРНОВИК
