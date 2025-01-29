age = int(input("enter age"))
day = input("enter today's day ").lower()

"""
price1 = 12
price2 = 8
if age < 18:
    print(price2)
else:
    print(price1)
"""
price = 12 if age >= 18 else 8
if day == "wednesday":
    price = price - 2
print(price)
