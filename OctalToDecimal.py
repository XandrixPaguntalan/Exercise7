octal = input("Enter a string of octal digits: ")
decimalValue = 0
base = 1
while octal:
    lastDigit = int(octal) % 10
    octal = int(octal) / 10
    decimalValue += lastDigit * base
    base = base * 8
print("The integer value is", decimalValue)