# A simple calculator app

# Creating this simple program because i made a note to myself on my desk to use
# conditionals in a while loop.

# First program committed to github.


def calculate(num1, operator, num2):
    """This function calculates all the operations in this program."""
    if operator == '+':
        return float(num1) + float(num2)
    # I started off with the addition operator, and then added the others below.
    elif operator == '-':
        return float(num1) - float(num2)
    elif operator == '/':
        return float(num1) / float(num2)
    elif operator == '*':
        return float(num1) * float(num2)


def number_check(num):
    """This function just error checks that only numbers can be used as a input."""
    try:
        float(num)
        return True
    except ValueError:
        print("Please enter numbers only.")
        return False


def run_app():
    """This does all the heavy lifting."""
    while True:
        number1 = input("Enter the first number: ")
        if number_check(number1):
            print(number1)
            op = input("Enter the operator: ")
            if op == '+' or op == '-' or op == '/' or op == '*':
                print(number1, op)
                number2 = input("Enter the second number: ")
                if number_check(number2):
                    if float(number2) == 0 and op == '/':
                        print("You cannot divide by 0")
                    else:
                        print(f"{number1} {op} {number2} = {calculate(number1, op, number2)}")
                        break
            else:
                print("Invalid operator")


run_app()
