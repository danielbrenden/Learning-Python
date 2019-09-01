# This program requires the user to inout their phone number, then prints that number using words.

phone = input ("Enter your phone number: ")
mapped_digits = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"


}
output = ""
for ch in phone:
    output += mapped_digits.get(ch, "!") + " "
print(output)
