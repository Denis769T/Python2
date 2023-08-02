# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
list_1 = [randint(0, 30) for i in range(20)]
list_2=list()
print(list_1) 
range_1=int(input("Ввод, нижнего предела промежутка:"))
range_2=int(input("Ввод, верхнего предела промежутка:"))
for i in range(0,len(list_1)):
    if  range_1<=list_1[i]<=range_2:
        list_2.append(i)
print(list_2)