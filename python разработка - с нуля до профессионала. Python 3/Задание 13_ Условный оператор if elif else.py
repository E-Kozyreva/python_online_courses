# Напишите код, который выводит сообщение: 'Enter any number'. Если было введено число 7, 
# должно выводиться сообщение: '7 is a lucky number! Today is your lucky day!', 
# если введено что-то другое - должно выводиться сообщение 'Thank you! Have a nice day!'
number = input()
if number == '7': print('7 is a lucky number! Today is your lucky day!')
else: print('Thank you! Have a nice day!')

# Напишите код, который выводит сообщение: 'Enter an integer number'. 
# Если было введено чётное число, должно выводиться сообщение: 'The number is even', 
# если было введено нечётное число, должно выводиться сообщение 'The number is odd'
number = int(input('Enter an integer number: '))
if number % 2 == 0: print('The number is even')
else: print('The number is odd')
