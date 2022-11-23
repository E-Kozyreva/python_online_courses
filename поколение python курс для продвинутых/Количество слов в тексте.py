# Напишите программу для определения общего количества различных слов в строке текста.

def delete_symbols(string):
    symbols = [".", ",", ";", ":", "-", "?", "!"]
    new_string = ""
    for symb in string:
        if symb not in symbols:
            new_string += symb
    list_of_words = new_string.split(" ")
    set_of_words = set()
    
    for word in list_of_words:
        set_of_words.add(word.lower())
    return len(set_of_words)


print(delete_symbols(input()))
