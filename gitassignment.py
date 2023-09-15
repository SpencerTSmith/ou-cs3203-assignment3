def sumlist(intlist):
    return sum(intlist)

def productlist(intlist):
    product = 1
    for i in intlist:
        product = product * i
    return product

def reverselist(xlist):
    return list(reversed(xlist))

input = input()
intlist = input.split()
intlist = [int(x) for x in intlist]

print(sumlist(intlist))
print(productlist(intlist))
print(reverselist(intlist))
#comment for commiting cuz i did 2 steps in one
<<<<<<< HEAD
<<<<<<< HEAD
=======

#comment for part10
>>>>>>> 87021b3 (Part 10)
=======

#comment for part10
>>>>>>> 87021b3 (Part 10)


