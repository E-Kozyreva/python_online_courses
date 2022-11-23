# Для настольной игры используются карточки с номерами от 1 до n. Одна карточка потерялась.
# Напишите программу, которая выводит номер потерянной карточки.

count_cards, available_cards = int(input()), []
all_cards = [card for card in range(1, count_cards + 1)]

for num in range(count_cards - 1):
    available_cards.append(int(input()))

for card in all_cards:
    if card not in available_cards:
        print(card)
        break
