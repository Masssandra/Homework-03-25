x = int(input("Enter the x value:"))

y = int(input("Enter the y value:"))


operation = input("Enter the arithmetic operation (+, -, * or /)")

if operation == "+":
    print("Your answer is", (x + y))
elif operation == "-":
    print("Your answer is", x - y)
elif operation == "*":
    print("Your answer is", x * y)
elif operation == "/":
    print("Your answer is", x / y)
else:
    print("You entered the wrong arithmetic action")