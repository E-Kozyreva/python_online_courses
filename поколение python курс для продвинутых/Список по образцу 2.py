# На вход программе подается число nn. Напишите программу, которая создает и выводит построчно вложенный список, 
# состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

count_lists, main_list = int(input()) + 1, []

for num in range(1, count_lists):
    main_list.append(num)
    print(main_list)
