# Напишите программу для вычисления суммы двух матриц.

def sum_matrix(i, j):
    matrix1, matrix2 = [], []
    
    for num in range(i):
        string = list(map(int, input().split()))
        matrix1.append(string)
        
    empty_string = input()
    
    for num in range(i):
        string = list(map(int, input().split()))
        matrix2.append(string)
            
    for s in range(i):
        string = []
        for c in range(j):
            string.append(matrix1[s][c] + matrix2[s][c])
        print(*string)
        string.clear()

data = list(map(int, input().split()))
sum_matrix(data[0], data[1])
