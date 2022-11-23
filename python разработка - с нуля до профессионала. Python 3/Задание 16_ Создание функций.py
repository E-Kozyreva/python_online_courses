# Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!' соответственно. 
# Сделайте по одному вызову каждой из функций
def cat_voice():
    print('Meow!')

def dog_voice():
    print('Woof!')

cat_voice()
dog_voice()

# Создайте функции cat_voice() and dog_voice(), которые возвращают значения 'Meow!' и 'Woof!' соответственно. 
# Выведите на экран 'Meow!' и 'Woof!' по 2 раза
def cat_voice():
    print('Meow!\n' * 2)

def dog_voice():
    print('Woof!\n' * 2)

cat_voice()
dog_voice()

# Создайте функцию get_voice() которая возвращает передаваемый ей в качестве параметра текст c восклицательным знаком.
def get_voice(voice = 'Hello!'):
    print(voice + '!')
get_voice('Hi')

# Создайте функцию, которая генерирует последовательность нечетных чисел в диапазоне от a до b (a и b включительно). 
# Значения a и b должны передаваться в качестве параметров. Результирующая последовательность должна возвращаться в форме объекта list. 
# Решите задание двумя способами - при помощи List Comprehension  и без него
#FIRST
def numbers(num_1, num_2):
    for num in range(num_1, num_2 + 1):
        print(num)
numbers(1, 10)
#SECOND
def numbers(num_1, num_2):
    list_of_numbers = [num for num in range(num_1, num_2 + 1)]
    print(*list_of_numbers)
numbers(1, 10)
