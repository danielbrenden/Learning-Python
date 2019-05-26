# This program asks user for two numbers and divides them and contains an exception if the user tries to divide by zero.

one = input('pick a number ')
two = input('pick another one ')
a = int(one)
b = int(two)

try:
    print(a / b)

except: ZeroDivisionError:\
    print("You can't divide by zero.")