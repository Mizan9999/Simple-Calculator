# Calculator
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def division(number1, number2):
    return  number1 / number2


print("Select an operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operation = input("Enter choice (1/2/3/4):  ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "1":
    print(add(num1, num2))

elif operation == "2":
    print(subtract(num1, num2))

elif operation == "3":
    print(multiply(num1, num2))

elif operation == "4":
    print(division(num1, num2))

