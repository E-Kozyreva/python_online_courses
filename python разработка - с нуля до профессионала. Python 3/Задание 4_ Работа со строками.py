# Создайте переменные, поместите в них значения - имя, фамилию и возраст. Выведите на экран следующее предложение: 
# "Hi! My name is имя фамилия, I'm возраст years old." Используйте конкатенацию переменных и строк.
name = 'Yikki'
surname = 'Kiro'
age = 17
print('Hi! My name is', name, surname, "I'm", age, 'years old.', sep = ' ')

# Выведите на экран текст детской песенки:
"""
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full

One for the master,
One for the dame,
And one for the little boy
Who lives down the lane

Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full """

# Отступите от левого края расстояние, равное двум табуляциям. Выполните перенос текста на новую строку двумя способами
part_1 = 'Baa, baa, black sheep,\nHave you any wool?\nYes sir, yes sir,\nThree bags full\n'
part_2 = 'One for the master,\nOne for the dame,\nAnd one for the little boy\nlives down the lane\n'
part_3 = 'Baa, baa, black sheep,\nHave you any wool?\nYes sir, yes sir,\nThree bags full'
print(part_1, part_2, part_3, sep = '\n')
