def sumAll(*args):
    return sum(args)

print(sumAll(1,2,3))
print(sumAll(5,4,6))
print(type(sumAll)) #function
print(type(sumAll(1,2))) #int