# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
# число ягод — на i-ом кусте выросло a[i] ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система 
# состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один 
# заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с 
# двух соседних с ним. Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым 
# кустом заданной во входном списке урожайности грядки.

from random import randint

bush = []
for i in range(int(input("Введите кол-во кустов: "))):
    bush.append(randint(1, 10))
print(bush)

a = int(input("Введите № куста: "))
sum = 0
sum = bush[a] + bush[a + 1] + bush[a - 1]
print(f"Собрано ягод: {sum}")