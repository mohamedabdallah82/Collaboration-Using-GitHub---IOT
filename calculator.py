number1 = int(input("Please Enter First Number: "))
number2 = int(input("Please Enter Second Number: "))
operation = input("Please Enter Operation: ")

match operation:
    case '+':
        print("add")
    case '-':
        print("sub")
    case '*':
        print("mul")
    case '/':
        print("dev")