# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.

length_and_width, sum_elements = int(input()), 0

for element in range(length_and_width):
    column = input().split(' ')
    sum_elements += int(column[element])

print(sum_elements)
