# Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.

def ArithmeticMean(numbers):
    arifm = 0
    ListWithArifm = []
  
    for nums in range(len(numbers)):
        arifm = sum(numbers[nums]) / len(numbers[nums])
        ListWithArifm.append(arifm)
  
    return print(ListWithArifm)
  
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
ArithmeticMean(numbers)
