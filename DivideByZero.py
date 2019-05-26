one = input('pick a number ')
two = input('pick another one ')
a = int(one)
b = int(two)

try:
    print(a / b)

except: ZeroDivisionError:\
    print("You can't divide by zero.")