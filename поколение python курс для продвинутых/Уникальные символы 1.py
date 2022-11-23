# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

def str_len(word):
    symbols = set(word.lower())
    print(len(symbols))


for _ in range(int(input())):
    str_len(input())
