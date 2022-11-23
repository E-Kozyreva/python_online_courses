# Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую на общее количество всех чисел.

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

total, counter = 0, 0

for list2 in list1:
    for index in range(len(list2)):
        counter += 1
        total += list2[index]
    
print(total / counter)
