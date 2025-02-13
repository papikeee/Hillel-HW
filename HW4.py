def main():
    num1 = int(input("Enter first digit:"))

    operation = input("Enter symbol (+, -, *, /):")

    num2 = int(input("Enter second digit:"))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error! We can't divide by zero")
            return
        result = num1 / num2
    else:
        print("Error!")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
