getallen = [1,2,3,5,7,8,10,12,13,14,15,16,21,22,23,24,26,30,31,32,33,43,44,46,47]

for (index, element) in enumerate(getallen, start=1):
    if element % 2 == 0 and index % 2 == 0: 
        print(index, element)
