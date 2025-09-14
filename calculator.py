number1 = int(input("Please Enter First Number: "))
number2 = int(input("Please Enter Second Number: "))
operation = input("Please Enter Operation: ")
result = 0

def add():
	result = number1 + number2

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

match operation:
    case '+':
        add()
	print(result)
    case '-':
        print(number1 -number2)
    case '*':
        print(number1 * number2)
    case '/':
        result = divide(number1, number2)
        print(f"{number1} / {number2} = {result}")
    case '_':
        print("Invalid operation! Please use +, -, *, or /")
