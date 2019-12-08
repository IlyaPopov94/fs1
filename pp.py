from random import choice

def F(N, *args):
    return [choice(args) for i in range(N)]

print(F(3, 'aaaaaaa', 'bbbbbbbbb', 'ccccccccccc', 'dddddddd', 'eee', 'fffffffff'))

lst = ['111101001', '151515151', '22222222222', '333', '4545454',
       '555555555', '666666666666', '777777777', '88888888888', '9999',
       '000', '111111', '222222', '3333333', '444',
       '555555555', '666666', '77777777', '88888', '9999999999']

list_F = F(100, *lst)
print(len(lst), len(list_F), list_F)

print()

# 2.

from collections import Counter

def max_count(lst):
    count = Counter(lst)
    return max(count, key=lambda x: count[x])

print(Counter(list_F))
print(*Counter(list_F).most_common(1))
print(Counter(list_F).most_common(1)[0][0])

print(max_count(list_F))

print()

# 3

def rare_letter(lst):
    lst = map(lambda x: x[0], lst)
    return Counter(lst).most_common()[-1:][0][0]

print(rare_letter(list_F))
list_F += ['xxxxxxxxx']  # Добавим редкую букву)
print(rare_letter(list_F))

print()