list = [1, 2, 3, 4, 5, 6, 7]
userInput = 1

while userInput != 0:
    even = 0
    odd = 0
    for i in list:
        if i == 0:
            continue
        elif i % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        print(f"{even} even numbers, {odd} odd numbers.")
    userInput = int(input("Input 0 to terminate: "))




