# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Enter n-size of chocolate: '))
m = int(input('Enter m-size of chocolate: '))
k = int(input('How many pieces do you need? '))

flag = 'yes' if ((k % n == 0) or (k % m == 0)) else 'no'

print(flag)
