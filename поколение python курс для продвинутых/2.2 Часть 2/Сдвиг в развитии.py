# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. 
# Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, 
# а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

string, number, numbers = input(), "",  []

for element in range(len(string)):
    if string[element] != " ":
        number += string[element]
    if string[element] == " ":
        numbers.append(number)
        number = ""
    if element == len(string) - 1:
        numbers.append(number)

print(numbers[-1], *numbers[:-1])
