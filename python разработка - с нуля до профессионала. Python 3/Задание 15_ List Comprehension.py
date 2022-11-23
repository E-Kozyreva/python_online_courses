# Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola'] создайте новый список содержащий вторую букву из каждой строки исходного списка. 
# Выведите новый список на печать. Решите задание двумя способами - при помощи List Comprehension и без него.
greetings = ['hello', 'hi', 'hey', 'hola']
new_greetings = []
for word in greetings:
    new_greetings.append(word[1])
print(*new_greetings)

# Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создайте новый список содержащий нечетные числа исходного списка. 
# Выведите новый список на печать. Решите задание двумя способами - при помощи List Comprehension и без него.
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_digits = [number for number in digits if number % 2 == 0]
print(*new_digits)
