# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. 
# Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

game = str(input() + "-" + input())

war = {"камень-камень":   "ничья", 
       "ножницы-ножницы": "ничья",
       "бумага-бумага":   "ничья",
       
       "камень-ножницы":  "Тимур",
       "ножницы-бумага":  "Тимур",
       "бумага-камень":   "Тимур",
       
       "камень-бумага":   "Руслан", 
       "ножницы-камень":  "Руслан",
       "бумага-ножницы":  "Руслан", }

print(war[game])
