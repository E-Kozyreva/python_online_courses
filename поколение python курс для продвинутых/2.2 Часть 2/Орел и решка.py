# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

game, count, max_count = input() + 'O', 0, 0

for letter in game:
    if letter == 'Р':
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0

if max_count > 0:
    print(max_count)
else:
    print(0)
