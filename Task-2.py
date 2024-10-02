while True:
    num1 = input("Please enter the first number: ")

    # Check  the first input input is integer or decimal number
    while True:
        if num1.count('.') <= 1 and num1.replace('.', '').isdigit():
            num1 = float(num1)
            break
        else:
            num1 = input("Invalid input, Please enter a valid number: ")

    num2 = input("Please enter the second number: ")

    # Check  the second input input is integer or decimal number
    while True:
        if num2.count('.') <= 1 and num2.replace('.', '').isdigit():
            num2 = float(num2)
            break
        else:
            num2 = input("Invalid input, Please enter a valid number: ")

    # Input the operation
    operation = input("Please enter the arithmetic operation ('+', '-', '*', '/'): ")

    # Check the operation
    if operation == "+":
        print(f"Result: {num1} {operation} {num2} = {num1 + num2}")

    elif operation == "-":
        print(f"Result: {num1} {operation} {num2} = {num1 - num2}")

    elif operation == "*":
        print(f"Result: {num1} {operation} {num2} = {num1 * num2}")

    elif operation == "/":
        if num2 != 0:
            print(f"Result: {num1} {operation} {num2} = {num1 / num2}")
        else:
            print("Division by zero is not allowed.")

    else:
        print("Invalid operation. Please choose ('+', '-', '*', '/').")

    ask = input("Do you want to perform another operation? (yes, no): ").lower()

    if ask not in ['y', 'yes']:
        print("Thank you for using simple calculator")
        break  