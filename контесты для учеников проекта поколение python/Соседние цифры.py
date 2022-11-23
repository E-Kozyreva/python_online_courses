# Напишите программу, которая определяет, содержит ли пятизначное число две одинаковые цифры, стоящие рядом.

number, answer = input(), False

for num in range(len(number) - 1):
    if number[num:num+2] == number[num:num+2][::-1]:
        answer = True

if answer == True:
    print('YES')
else:
    print('NO')
