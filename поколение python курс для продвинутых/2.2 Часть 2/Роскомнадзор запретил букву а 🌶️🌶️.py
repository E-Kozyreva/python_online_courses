# Необходимо написать программу, реализующую алгоритм написания этой песни. Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, 
# если она встречается в строке текста, а очередную строку отображает уже без этой буквы.

word = input() + " запретил букву"

for alphabet in range(ord("а"), ord("а") + 32):
    string = ""
    if chr(alphabet) in word:
        print(word, chr(alphabet))
        for symbol in word:
            if symbol != chr(alphabet):
                string += symbol
        word = " ".join(string.split())
