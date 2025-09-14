number1 = int(input("Please Enter First Number: "))
number2 = int(input("Please Enter Second Number: "))
operation = input("Please Enter Operation: ")
result = 0

def add():
	result = number1 + number2

match operation:
    case '+':
        add()
	print(result)
    case '-':
        print(number1 -number2)
    case '*':
        print("mul")
    case '/':
        print("dev")
