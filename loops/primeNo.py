number = 22

for i in range(2,number):
    if (number % i) == 0:
        print("Not a prime")
        break
    else:
        print("Prime number")
        break