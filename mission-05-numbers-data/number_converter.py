
def number_converter():
    print("===== NUMBER SYSTEM CONVERTER =====")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        number = int(input("Enter decimal number: "))
        print("Binary:", bin(number)[2:])

    elif choice == "2":
        number = int(input("Enter decimal number: "))
        print("Octal:", oct(number)[2:])

    elif choice == "3":
        number = int(input("Enter decimal number: "))
        print("Hexadecimal:", hex(number)[2:].upper())

    elif choice == "4":
        number = input("Enter binary number: ")
        print("Decimal:", int(number, 2))

    elif choice == "5":
        number = input("Enter octal number: ")
        print("Decimal:", int(number, 8))

    elif choice == "6":
        number = input("Enter hexadecimal number: ")
        print("Decimal:", int(number, 16))

    else:
        print("Invalid choice!")


number_converter()
