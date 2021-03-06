# -*- coding: utf-8 -*-

# Найти наибольшее из двух чисел

# Вариант 1
# a = int(input())
# b = int(input())
# if a >= b:
#     print(a)
# else:
#     print(b)

# Вариант 2
# a = int(input())
# b = int(input())
# m = a
# if b > m:
#     m = b
# print(m)

# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки,
# но пересыпать тоже вредно и не стоит спать более B часов.
# Сейчас Аня спит H часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
# Если Аня спит менее A часов, выведите “Недосып”, если же более B часов,
# то выведите “Пересып”.
# Получаемое число A всегда меньше либо равно B.
# На вход программе в три строки подаются переменные в следующем порядке: A, B, H.
# Проверка:
# Sample Input 1: 6,10,8 Sample Output 1: Это нормально
# Sample Input 2: 7,9,10 Sample Output 2: Пересып
# Sample Input 3: 7,9,2  Sample Output 3: Недосып

# Вариант 1
# A = int(input())
# B = int(input())
# H = int(input())
# if A <=H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# elif H > B:
#     print('Пересып')
#
# Вариант 2
# A = int(input())
# B = int(input())
# H = int(input())
# if A <=H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# else:
#     print('Пересып')

# Требуется определить, является ли данный год високосным.
# Напомним, что год является високосным, если его номер кратен 4,
# но при этом не кратен 100, или если он кратен 400
# (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
# Программа должна корректно работать на числах 1900≤n≤3000.
# Выведите "Високосный" в случае, если считанный год является високосным
# и "Обычный" в обратном случае
# (не забывайте проверять регистр выводимых программой символов).
# Проверка
# Sample Input 1: 2100 Sample Output 1: Обычный
# Sample Input 2: 2000 Sample Output 2: Високосный

# Вариант 1
# n = int(input())
# if (n%4 == 0 and n%100 != 0) or n%400 == 0:
#     print('Високосный')
# else:
#     print('Обычный')