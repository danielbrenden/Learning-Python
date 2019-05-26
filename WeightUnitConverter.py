weight = int(input("What is your weight? "))
metric = input("(L)bs or (K)gs? ")

if metric.upper() == "L":
    final_weight = weight * 0.453592
    print(f'You are {final_weight} kilograms!')

else:
    final_weight = weight / 0.453592
    print(f'You are {final_weight} pounds!')