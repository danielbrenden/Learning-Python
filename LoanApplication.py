# This is a program to determine if you qualify for a loan based on income and credit score.

income = input('What is your yearly income? ex. "50000" ')
credit = int(input('What is your credit score? '))

x = int(income)
y = int(credit)

if x >= 20000 or y >= 750:
    print("You've qualified!")

else: print("Sorry, you did not qualify.")