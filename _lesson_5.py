# -*- coding: utf-8 -*-

# Прочитать пять пар чисел и вывести их произведение
# 1) Если ввели два нуля то мы завершаем программу
# 2) Если введен один ноль мы игнорируем данный ввод

# i = 0
# while i < 5:
#     a,b = input().split()
#     a = int(a)
#     b = int(b)
#     if a == 0 and b == 0:
#         break
#     elif a == 0 or b == 0:
#         continue
#     print(a * b)
#     i += 1

# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль.
# Проверка:
# Sample Input 1: 12, 4, 2, 58, 112 Sample Output 1: 12, 58
# Sample Input 2: 101 Sample Output 2:
# Sample Input 3: 1, 2, 102 Sample Output 3:

# Вариант 1
# a = 1
# while True:
#     a = int(input())
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     else:
#         print(a)

