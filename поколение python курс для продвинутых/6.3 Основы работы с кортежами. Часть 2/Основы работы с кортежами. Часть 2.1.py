# Дополните приведенный код так, чтобы он вывел произведение элементов кортежа numbers.

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
multiplication = 1

for _ in range(len(numbers)):
    multiplication *= numbers[_]
    
print(multiplication)
