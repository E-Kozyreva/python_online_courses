# На вход программе подается число nn. Напишите программу, которая создает и выводит построчно список, состоящий 
# из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

count_lists = int(input())
main_list = list(range(1, count_lists + 1))

for _ in range(count_lists):
    print(main_list)
