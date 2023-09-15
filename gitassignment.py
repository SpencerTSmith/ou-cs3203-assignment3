def sumlist(list):
    return sum(list)

def productlist(list):
    product = 1
    for i in list:
        product = product * i
    return product

input = input()
list = input.split()
list = [int(x) for x in list]

print(sumlist(list))
print(productlist(list))


