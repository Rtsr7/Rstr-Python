# Decimal to binary
decimal = int(input("Enter the number here: "))
print("Decimal: ", decimal, "\nBinary: ", bin(decimal))

# Binary to decimal
values = input("For Binary to integer press y: ")
if (values == "y" or values == "Y"):
    binary = input("Enter the binary number: ")
    print("Binary: ", binary, "\nDecimal: ", int(binary, 2))
else:
    print("Error \nYou didn't press y")
