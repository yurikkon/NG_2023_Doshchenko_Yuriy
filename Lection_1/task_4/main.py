print("Choise operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. degree")
print("6. root")


choice = int(input("Enter number operaton (1/2/3/4): "))


if choice == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1 + num2)

elif choice == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1 - num2)

elif choice == 3:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1 * num2)

elif choice == 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1 / num2)

elif choice == 5:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1 ** num2)

elif choice == 6:
    num1 = float(input("Enter number: "))
    print(num1 ** 0,5)