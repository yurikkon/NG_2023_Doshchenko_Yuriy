last_number = int(input("Enter any number: "))


result_divide = []


prime_numbers = []


for number in range(1,last_number + 1):
    divides = []
    for divide in range(1, number + 1):
        if number % divide == 0:
            divides.append(divide)
    result = f"{number}  {divides}"
    result_divide.append(result)
    
    if len(divides) == 2:
        prime_numbers.append(number)


for string in result_divide:
    print(string)


print(prime_numbers)