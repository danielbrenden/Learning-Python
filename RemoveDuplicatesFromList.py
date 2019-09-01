# This program removes duplicates from a list of numbers via the append method and prints the result.

numbers = [2, 4, 5, 6, 5, 7, 8, 9, 9]
unique_numbers = []
for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
print (unique_numbers)
