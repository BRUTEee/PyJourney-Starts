def calculator():
    print("\n Calculator 🧮")
    print("Operations: +  -  *  /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        else:
            result = "Invalid operator!"
        
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
