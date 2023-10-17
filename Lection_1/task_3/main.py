print("Write 1 or 2: ")
choise = int(input("1-convert degrees Celcius to fahrenheit\n2-fahrenheit to degrees Celcius: "))



if choise == 1:
    degrees = float(input("write how many degrees Celcius you want to convert: "))
    fahrenheit = (degrees * 1.8) + 32
    print("that's how much it will be in Fahrenheit: " + str(fahrenheit))
elif choise == 2:
    fahrenheit = float(input("write how many fahrenheit you want to convert: "))
    degrees = (fahrenheit - 32) / 1.8
    print("that's how much it will be in degrees Celcius: " + str(degrees))