response = 0
int1 = 0
int2 = 0
result = 0
year = 0



def menu():
    print("\n\nOption 1: Number mathematics")
    print("Option 2: Leap years")
    print("Option 3: Bitwise mathematics")
    print("Option 4: Exit\n")


menu()
response = int(input("Choose which option by entering corresponding number in numeric form: "))
print("\n")

while response != 4:

    if response == 1:
        int1 = int(input("First number: "))
        int2 = int(input("Second number: "))

        if int1 > int2:
            result = int1 - int2
        elif int1 < int2:
            result = int1 + int2
        else:
            result = int1 * int2

        print(result)
    elif response == 2:
        year = int(input("Enter year: "))

        if (year % 4) == 0:
            if (year % 100) == 0 and (year % 400) == 0:
                print(f"{year} is a leap year.")
            elif (year % 100) == 0:
                print(f"{year} is not a leap year.")
            else:
                print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    elif response == 3:
        int1 = int(input("First number: "))
        int2 = int(input("Second number: "))

        print("Bitwise AND:", int1 & int2)
        print("Bitwise OR:", int1 | int2)
        print("Bitwise NOT for first number:", ~(int1) + 1)
        print("Bitwise shift for second number with LEFT shift by one bit", f"'{(int2 << 1)}'", f"then two bit shift RIGHT, resulting in '{((int2<<1)>>2)}'")

    menu()
    response = int(input("Choose which option by entering corresponding number in numeric form: "))
    print("\n")

