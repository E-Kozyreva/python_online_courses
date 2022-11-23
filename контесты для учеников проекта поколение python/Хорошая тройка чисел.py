# Назовем тройку чисел хорошей, если среди них есть хотя бы одно четное и хотя бы одно нечетное число.
# Напишите программу, которая определяет является ли тройка чисел хорошей или нет.

num_1, num_2, num_3 = int(input()), int(input()), int(input())
count_even_num, count_odd_num= 0, 0
all_numbers = [num_1, num_2, num_3]

for num in all_numbers:
    if num % 2 == 0:
        count_even_num +=1
    elif num % 2 != 0:
        count_odd_num += 1

if count_odd_num > 0 and count_even_num > 0:
    print('YES')
else:
    print('NO')
