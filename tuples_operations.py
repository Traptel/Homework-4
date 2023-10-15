first = (1, 2, 3)
second = (3, 4, 5)
# Task A
lst_tuple = list(first + second)
print(lst_tuple)
# Task B
t_result = (lst_tuple, first[::-1], second[::-1])
print(t_result)
# Task C
print(t_result[0][2])
print(t_result[1][2])
print(t_result[2][2])
