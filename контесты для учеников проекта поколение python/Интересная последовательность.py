# Рассмотрим последовательность чисел в которой каждое натуральное число k встречается ровно k раз:
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...
# 1,2,2,3,3,3,4,4,4,4,...
# Напишите программу, которая по данному натуральному числу k выведет первые k членов этой последовательности.

number, count, line = int(input()), 0, ''
sequence = []

for num in range(1, number + 1):
    letter = str(num)
    for count_letter in range(1, num + 1):
        sequence.append(letter)
        
while count < number:
    print(sequence[count], end=' ')
    count += 1
