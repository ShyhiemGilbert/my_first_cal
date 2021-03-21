num1 = float(input('Enter First Number: '))
operation = input('Enter the operation: ')
num2 = float(input('Enter Second Number: '))


# Addition
if operation == '+':
    print(num1 + num2)
# Subtract
elif operation == '-':
    print(num1 - num2)
# Division
elif operation == '/':
    print(num1 / num2)
# Times
elif operation == '*':
    print(num1 * num2)
else:
    print('Invalid operation')
