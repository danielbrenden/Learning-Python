def convert(string):
    try:
        return float(string)

    except ValueError:
        print("Please enter a proper string to convert")

c = convert("66")
print(c)
