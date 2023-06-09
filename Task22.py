"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
Пример, 
Input - 11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
Output - 6 12
"""
n, m  = int(input('Введите кол-во элементов в первом наборе: ')), int(input('Введите кол-во элементов во втором наборе: '))
first_list = [int(num) for num in input().split()]
second_list = [int(num) for num in input().split()]

first_set = set(first_list)
second_set = set(second_list)

print(*sorted(first_set.intersection(second_set)))

