
number = int(input("Enter a positive decimal number: "))

if number < 0:
    print("Please enter a positive number.")
else:
    print("Binary:", bin(number))
    print("Hexadecimal:", hex(number))
