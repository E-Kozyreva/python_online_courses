# Уравнение параболы имеет вид y =ax^2 + bx + c. Напишите программу, которая по введенным значениям a, b, c определяет и выводит вершину параболы.

def TopOfParabola(a, b, c):
    x = -(b / (2*a))
    y = ((4 * a * c) - (b ** 2)) / (4 * a)
    
    return x, y

a, b, c = int(input()), int(input()), int(input())
print(TopOfParabola(a, b, c))
