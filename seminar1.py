# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
#    является ли одно число квадратом другого.
    
#    *Примеры:* 
    
#    - 5, 25 -> да
#    - 4, 16 -> да
#    - 25, 5 -> да
#    - 8,9 -> нет


# n1 = int(input())
# n2 = int(input())

# if n1 ** 2 == n2:
#     print(True)
# elif n2 ** 2 == n1:
#     print(True)
# else:
#     print(False)


# 2. Напишите программу, которая на вход принимает 5 чисел
#     и находит максимальное из них.
    
#    Примеры:
    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

# max = -1
# for i in range(5):
#     n = int(input())
#     if max < n:
#         max = n
# print (max)

# Метод Флажка (break)

# flag = True
# i = 0
# while flag:
#     i += 1
#     if i == 11:
#         flag = False
# print(i)


#3. Напишите программу, которая будет принимать на вход дробь и 
#   показывать первую цифру дробной части числа.
    
#    *Примеры:*
    
#    - 6,78 -> 7
#    - 5 -> нет
#    - 0,34 -> 3

# n = float(input())
# if int(n) == n:
#     print('no')
# else:
#     print(int(n * 10)  % 10)

#4. Напишите программу, которая принимает на вход число и проверяет, 
#   кратно ли оно 5 и 10 или 15, но не 30.

# n = int(input())
# if (n % 5 == 0 and n % 10 == 0) or (n % 15 == 0 and n % 30 != 0):
#     print('yes')
# else:
#     print('no')

n = int(input())
max1 = n
max2 = -1
while n != 0:
    n = int(input())
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n
print(max2)
