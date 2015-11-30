# -*- coding: utf-8 -*-

# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки сначала максимальное,
# потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.
# Проверка:
# Sample Input 1: 8,2,14 Sample Output 1: 14,2,8
# Sample Input 2: 23,23,21 Sample Output 2: 23,21,23

# Вариант 1
# a = int(input())
# b = int(input())
# c = int(input())
# if b <= a >= c:
#     if b >= c:
#         print(a)
#         print(c)
#         print(b)
#     elif c > b:
#         print(a)
#         print(b)
#         print(c)
# if a < b >= c:
#     if a >= c:
#         print(b)
#         print(c)
#         print(a)
#     elif c > a:
#         print(b)
#         print(a)
#         print(c)
# if b < c > a:
#     if a >= b:
#         print(c)
#         print(b)
#         print(a)
#     elif b > a:
#         print(c)
#         print(a)
#         print(b)

# В институте биоинформатики по офису передвигается робот. Недавно студенты из группы
# программистов написали для него программу, по которой робот, когда заходит в комнату,
# считает количество программистов в ней и произносит его вслух: "n программистов".
# Для того, чтобы это звучало правильно, для каждого n нужно использовать верное окончание
# слова.
# Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное),
# выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
# для того, чтобы робот мог нормально общаться с людьми, например: 1 программист,
# 2 программиста, 5 программистов.
# В комнате может быть очень много программистов.
# Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.
# Проверка:
# Sample Input 1: 5 Sample Output 1: 5 программистов
# Sample Input 2: 0 Sample Output 2: 0 программистов
# Sample Input 3: 1 Sample Output 3: 1 программист
# Sample Input 4: 2 Sample Output 4: 2 программиста

# Вариант 1
# Это цикл для проверки
# s = 1000
# n = 0
# while n <= s:
#     if n == 11 or n == 12 or n == 13 or n == 14:
#         print(n,'программистов')
#     elif n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14:
#         print(n,'программистов')
#     elif n%10 == 1:
#         print(n,'программист')
#     elif n%10 == 2 or n%10 == 3 or n%10 == 4:
#         print(n,'программиста')
#     elif n%10 == 0 or n%10 == 5 or n%10 == 6 or n%10 == 6 or n%10 == 7 or n%10 == 8 or n%10 == 9:
#         print(n,'программистов')
#     n += 1

# Решение
# n = int(input())
# if n == 11 or n == 12 or n == 13 or n == 14:
#     print(n,'программистов')
# elif n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14:
#     print(n,'программистов')
# elif n%10 == 1:
#     print(n,'программист')
# elif n%10 == 2 or n%10 == 3 or n%10 == 4:
#     print(n,'программиста')
# elif n%10 == 0 or n%10 == 5 or n%10 == 6 or n%10 == 6 or n%10 == 7 or n%10 == 8 or n%10 == 9:
#     print(n,'программистов')

# Паша очень любит кататься на общественном транспорте, а получая билет,
# сразу проверяет, счастливый ли ему попался. Билет считается счастливым,
# если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
# которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают,
# и "Обычный", если суммы различны.
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
# Проверка:
# Sample Input 1: 090234 Sample Output 1: Счастливый
# Sample Input 2: 123456 Sample Output 2: Обычный

# Вариант 1
# a = int(input())
# b = a//1000
# c = a%1000
# x1 = b//100
# x2 = (b%100)//10
# x3 = b%10
# y1 = c//100
# y2 = (c%100)//10
# y3 = c%10
# if (x1+x2+x3) == (y1+y2+y3):
#     print('Счастливый')
# else:
#     print('Обычный')

