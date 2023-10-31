def add(x, y):
    """
    This function adds two numbers.
    """
    return x + y

def subtract(x, y):
    """
    This function subtracts y from x.
    """
    return x - y

def multiply(x, y):
    """
    This function multiplies two numbers.
    """
    return x * y

def divide(x, y):
    """
    This function divides x by y.
    If y is 0, it returns a message indicating division by zero is not allowed.
    """
    if y == 0:
        return "Cannot divide by zero"
    return x / y

if __name__ == "__main__":
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result:", add(num1, num2))
            elif user_input == "subtract":
                print("Result:", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result:", multiply(num1, num2))
            elif user_input == "divide":
                result = divide(num1, num2)
                print("Result:", result)
        else:
            print("Invalid input")
