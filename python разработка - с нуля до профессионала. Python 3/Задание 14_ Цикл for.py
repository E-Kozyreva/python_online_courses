# Используйте цикл for для вычисления суммы всех чётных чисел в диапазоне от 10 до 30 (включая крайние значения). Выведите результат на печать
sum_of_even_numbers = sum([num for num in range(10, 31, 2)])
print(sum_of_even_numbers)

# Получите от пользователя число на вводе и используйте цикл for для вывода на экран текста 'Hello!' столько же раз
count = int(input())
for user in range(count):
    print('Hello!')
