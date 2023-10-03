choise = int(input("Write 1 if you want to convert degrees to fahrenheit\nWrite 2 if you want to convert fahrenheit to degrees: "))


if choise == 1:
    degrees = float(input("write how many degrees you want to convert: "))
    fahrenheit = (degrees * 1.8) + 32
    print("that's how much it will be in Fahrenheit: " + str(fahrenheit))


else:
    fahrenheit = float(input("write how many fahrenheit you want to convert: "))
    degrees = (fahrenheit - 32) / 1.8
    print("that's how much it will be in degrees: " + str(degrees))