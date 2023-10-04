firstnumber = int(input("write coefficient a number: "))
secondnumber = int(input("write coefficient b number: "))
thirtnumber = int(input("write coefficient c number: "))
disc = (secondnumber * secondnumber) - (4 * (firstnumber * thirtnumber))
print(disc)
if disc <= 0:
    print("sorry disc < 0 bad coefficient")
if disc == 0:
    firstanswer = - (secondnumber / (2*firstnumber))
    print( firstanswer)
if disc >= 0:
    firstanswer = ((- secondnumber) - (disc ** 0.5)) / (2*firstnumber)
    secondanswer = ((- secondnumber) + (disc ** 0.5)) / (2*firstnumber)
    print(firstanswer)
    print(secondanswer)