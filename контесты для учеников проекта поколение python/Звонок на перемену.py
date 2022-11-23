# Продолжительность каждого урока в онлайн-школе BEEGEEK 45 минут, а перемены между уроками – 55 минут. 
# Первый урок начинается ровно в 8 часов утра. Напишите программу, определяющую во сколько заканчивается n-ый урок?

num_of_lesson, lesson, time = int(input()), 45, 0
hours, minutes = 0, 0
time = lesson * num_of_lesson

if num_of_lesson == 1:
    print('8 45')

elif num_of_lesson > 1:
    time = (num_of_lesson * lesson) + (5 * (num_of_lesson - 1))
    hour, minutes = time // 60, time % 60
    print(hour + 8, minutes)
