# Китайский гороскоп назначает животным годы в 1212-летнем цикле. Один 1212-летний цикл показан в таблице ниже. 
# Таким образом, 20122012 год будет очередным годом дракона.
# Напишите программу, которая считывает год и отображает название связанного с ним животного. 
# Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.

year = int(input())
zodiac = {0: 'Обезьяна', 6: 'Тигр',
          1: 'Петух',    7: 'Заяц',
          2: 'Собака',   8: 'Дракон',
          3: 'Свинья',   9: 'Змея',
          4: 'Крыса',    10: 'Лошадь',
          5: 'Бык',      11: 'Овца', }
print(zodiac[year % 12])
