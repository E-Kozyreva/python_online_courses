# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице. 
# Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.
# Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, 
# но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.

length, width, matrix = int(input()), int(input()), []

for l_th in range(length):
    column = []
    for w_th in range(width):
        column.append(input())
    matrix.append(column)

for element in matrix:
    print(*element)

print()

for w_th in range(width):
    for l_th in range(length):
        print(matrix[l_th][w_th], end=' ')
    print()
