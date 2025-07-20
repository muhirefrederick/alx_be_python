#manth calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Match case calculator
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case _ if operation == "+":
        result = num1 + num2  
    case _ if operation == "-":
        result = num1 - num2  
    case _ if operation == "*":
        result = num1 * num2
    case _ if operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    case _:
        result = "Error: Invalid operation"
print(f"The result is {result}.")