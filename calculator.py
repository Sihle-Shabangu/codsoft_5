def main():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Not a valid number")
        return

    op = input("Enter operator: ")

    if op in ("+", "-", "*", "/"):
        result = perform_operation(op, num1, num2)
        print(result)
    else:
        print("Invalid operator")


def perform_operation(operator, n, m):
    if operator == "+":
        return addition(n, m)
    elif operator == "-":
        return subtraction(n, m)
    elif operator == "*":
        return multiplication(n, m)
    elif operator == "/":
        return division(n, m)


def addition(n, m):
    return n + m


def subtraction(n, m):
    return n - m


def multiplication(n, m):
    return n * m


def division(n, m):
    try:
        return n / m
    except ZeroDivisionError:
        return "Cannot divide by Zero"


if __name__ == "__main__":
    main()
