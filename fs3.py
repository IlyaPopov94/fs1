'''
#Задача 1
#Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

i  = 0
for i in range(1, 6):
    print(i, 0)
    i += 1
'''

#Задача 2
#Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
i = 0
s = 0
for i in range(1, 11):
    print('№', i)
    num = 100
    while num/10 > 1:
        num = int(input('Введите цифру: '))
    if num == 5:
        s += 1
print('Цифру 5 Вы ввели', s, 'раз.')
'''
'''
#Задача 3
#Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
sum = 0

for i in range(1, 101):
     sum += i
print(sum)
'''
'''
#Задача 4
#Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
mult = 1
for i in range(1,11):
    mult *= i
print(mult)
'''
#Задача 5
#Вывести цифры числа на каждой строчке.
'''

integer_number = 2129

print(integer_number%10,integer_number//10)

while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10

'''
'''
#Задача 6
#Найти сумму цифр числа.
num = int(input('Введите число: '))
sum = 0

while num > 0:
    sum += num % 10
    num = num//10
print(sum)
'''
'''
#Задача 7
#Найти произведение цифр числа.
num = int(input('Введите число: '))
mult = 1

while num > 0:
    mult *= num%10
    num = num//10
print(mult)
'''
'''
#Задача 8
#Дать ответ на вопрос: есть ли среди цифр числа 5?
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''
'''
#Задача 9
#Найти максимальную цифру в числе

print()
print('Задача 9')
print()
max = 0
num = int(input('Введите число: '))
while num > 0:
    if num%10 >= max:
        max = num % 10
    num = num//10
print(max)
'''
'''
#Задача 10
#Найти количество цифр 5 в числе
num = int(input('Введите число: '))
five = 0
while num > 0:
    if num%10 == 5:
        five +=1
    num = num//10
print('Количество цифр 5 в числе:', five)
'''