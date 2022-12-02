# Напишите программу, которая принимает на вход координаты точки (X и Y), причем Х ≠ 0 и Y ≠ 0 и выдает номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4 -> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите первую координату x≠0: '))
y = int(input('Введите вторую координату y≠0: '))
if x>0 and y>0:
    print('Эта точка лежит в первой четверти')
elif x<0 and y>0:
    print('Эта точка лежит во второй четверти')
elif x<0 and y<0:
    print('Эта точка лежит в третьей четверти')
else:
    print('Эта точка лежит в четвертой четверти')