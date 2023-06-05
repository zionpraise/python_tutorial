def add (a, b):
    answer = a + b
    print(a , "+" , b , "=" , answer, "\n")

def sub (a, b):
    answer = a - b
    print(a , "-" , b , "=" , answer, "\n")

def mul (a, b):
    answer  = a * b
    print(a , "*" , b , "=" , answer, "\n")

def div (a, b):
    answer = a / b
    print(a, "/" , b , "=" , answer, "\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Divition")
    print("Q. Quite")
    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A" :
        print("Addition")
        a = int(input("Input frist number: "))
        b = int(input("Input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B" :
        print("subtraction")
        a = int(input("Input frist number: "))
        b = int(input("Input second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C" :
        print("Multiplication")
        a = int(input("Input frist number: "))
        b = int(input("Input second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D" :
        print("division")
        a = int(input("Input frist number: "))
        b = int(input("Input second number: "))
        div(a, b)
    elif choice == "q" or choice == "Q" :
        print("Program ended")
        quit()