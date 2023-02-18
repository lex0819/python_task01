# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

num_srt = input('Enter number of ticket: ')

print(num_srt)

def sum_of_ticket(num_arr):
    sum = 0
    print(type(num_arr))
    for char in num_arr:
      sum += int(char)

    return sum

first_sum = sum_of_ticket(num_srt[0:3])
last_sum = sum_of_ticket(num_srt[3:])

flag = 'Yes' if first_sum == last_sum else 'No'

print(f"{flag}")