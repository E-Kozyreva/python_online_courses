# Дана последовательность чисел длинной N. Найти последнее (правое) вхождение числа X в неё или вывести -1, если число X не встречалось.

def findrightx(seq, x):
  ans = -1
  for i in range(len(seq)):
    if seq[i] == x:
      ans = i
  return 
