# На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии 
# со стандартным американским соглашением о запятых в больших числах.

number = input()[::-1]
number_SAC, category = '',  0

for digit in number:
    number_SAC += digit
    if category % 3 == 2:
        number_SAC += ','
    category += 1

print(number_SAC[::-1].strip(','))
