# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


num_srt = input('Enter number: ')

print(num_srt)

sum = 0
for char in num_srt:
    sum += int(char)

print(f"sum is {sum}")