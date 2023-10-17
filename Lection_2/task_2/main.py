list1 = input("Write your list: ").split()
list2 = []
print (list1)
for element in list1:
    if element.isdigit(): 
        list2.append(element)
print("it`s all number in your list " + str(list2))
