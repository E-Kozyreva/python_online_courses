# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

def str_len(word):
    symbols = set(word.lower())
    print(len(symbols))


n, string = int(input()), input() 
for _ in range(n - 1):
    string += input()
str_len(string.lower())
