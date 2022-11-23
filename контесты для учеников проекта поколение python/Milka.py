# На вход программе подаются натуральные числа n, mm и k. Напишите программу, которая будет определять, 
# можно ли от шоколадки размером n n×m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

height, width, parts = int(input()), int(input()), int(input())
table_1, table_2 = [], []

for num in range(1, height + 1):
    table_1.append(num * width)

for num in range(1, width + 1):
    table_2.append(num * height)

if parts in table_1 or parts in table_2:
    print('YES')
else:
    print('NO')
