num1 = int(input("Enter frist number: "))
num2 = int(input("Enter second number: "))
oprator = input("Enter operator: ")

if oprator == '+':
    print(num1 + num2)
elif oprator == '-':
    print(num1 - num2)
elif oprator == '*':
    print(num1 * num2)
elif oprator == '/':
    print(num1 / num2)
else :
    print("Invalid oprator")
