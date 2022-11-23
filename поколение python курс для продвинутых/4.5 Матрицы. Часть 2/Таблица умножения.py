# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице. 
# Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

def mult(start, end):
    index, matrix = 0, []
    for i in range(start):
        for j in range(end):
            matrix.append(i * j)
    
    for _ in range(start):
        print(*matrix[index:index + end])
        index += end
            
            
mult(int(input()), int(input()))
