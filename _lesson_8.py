# -*- coding: utf-8 -*-

# Напишите программу, на вход которой подается одна строка с целыми числами. Программа
# должна вывести сумму этих чисел.
# Используйте метод split строки.
# Проверка:
# Sample Input: 4 -1 9 3 Sample Output: 15

# a = (int(i) for i in input().split())
# s = 0
# for i in a:
#     s += i
# print(s)


# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка. Например,
# если на вход подаётся список "1 3 5 6 10", то на выход ожидается
# список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
# Проверка:
# Sample Input 1: 1 3 5 6 10 Sample Output 1: 13 6 9 15 7
# Sample Input 2: 10 Sample Output 2: 10

# Вариант 1.1
# a = [int(i) for i in input().split()]
# for i in range(0,len(a)):
#     if len(a) == 1:
#         print(a[i])
#     elif i < len(a)-1:
#         print(a[i-1]+a[i+1],end=' ')
#     else:
#         print(a[-2]+a[0],end=' ')

# Вариант 1.2
# a = [int(i) for i in input().split()]
# for i in range(0,len(a)):
#     if len(a) == 1:
#         print(a[i])
#     elif i < len(a)-1:
#         print(a[i+1]+a[i-1],end=' ')
#     else:
#         print(a[0]+a[i-1],end=' ')

# Вариант 2
# a = [int(i) for i in input().split()]
# b = []
# for i in range(0,len(a)):
#     if len(a) == 1:
#         c = a[i]
#         b.append(c)
#     elif i < len(a)-1:
#         c = (a[i+1]+a[i-1])
#         b.append(c)
#     else:
#         c = (a[0]+a[i-1])
#         b.append(c)
# print(' '.join(str(i) for i in b))

# Вариант 3 (От Коляна)
# my_input = [int(i) for i in input().split()]
# my_output = []
# a = 0
#
# for i in range(0, len(my_input)):
#
#     # if input list consists of one element
#     if len(my_input) == 1:
#         a = my_input[0]
#
#     # if input list consists of many elements
#     else:
#         index_first = i + 1
#         index_second = i - 1
#
#         # to avoid exception 'index out of range'
#         if i >= len(my_input) - 1:
#             index_first = 0
#
#         a = my_input[index_first] + my_input[index_second]
#
#     my_output.append(a)


# Напишите программу, которая принимает на вход список чисел в одной строке и выводит
# на экран в одну строку значения, которые повторяются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
# Проверка:
# Sample Input 1: 4 8 0 3 4 2 0 3 Sample Output 1: 0 3 4
# Sample Input 2: 10 Sample Output 2:
# Sample Input 3: 1 1 2 2 3 3 Sample Output 3: 1 2 3
# Sample Input 4: 1 1 1 1 1 2 2 2 Sample Output 4: 1 2

# Вариант 1.1
# myinput = [int(i) for i in input().split()]
# myoutput = []
# myinput.sort()
# for i in range(1,len(myinput)):
#     if myinput[i] == myinput[i-1]:
#         if myinput[i] not in myoutput:
#             myoutput.append(myinput[i])
#     else:
#         continue
# print(' '.join(str(i) for i in myoutput))

# Вариант 1.2
# a = [int(i) for i in input().split()]
# b = []
# a.sort()
# for i in range (1,len(a)):
#     if a[i] == a[i-1]:
#         if a[i] not in b:
#             b.append(a[i])
# c = ' '.join(str(i) for i in b)
# print(c)