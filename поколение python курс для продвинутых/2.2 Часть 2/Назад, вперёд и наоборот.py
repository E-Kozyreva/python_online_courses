# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. 
# Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). 
# Если в списке нечетное количество элементов, то последний остается на своем месте.

numbers = list(input().split())
count_numbers, new_order, index_num = len(numbers), [], 0

for num in range(1, count_numbers, 2):
    new_order.append(numbers[num])
    new_order.append(numbers[index_num])
    index_num += 2

if count_numbers % 2 == 0:
    print(*new_order)
else:
    print(*new_order, numbers[-1])
