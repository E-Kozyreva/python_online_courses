# Создайте объект tuple, описывающий компьютер и распакуйте его в соответствующие переменные. 
# Выведите переменные вызвав функцию print() один раз
computer = ('Model Series: Spectre X360 Convertible 13', 
            'Processor: Intel Core i5 8265U 1.6 GHz', 
            'SSD capacity: 512 GB', 
            'Diagonal/Resolution: 13.3"/1920x1080 pixels.', )
for specifications in range(len(computer)):
    print(computer[specifications])
