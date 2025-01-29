"""
order ="small"
option = "with extra short of expresso"

if order == "small" or "medium" or "large":
    if option == "with extra short of expresso":
        print("Order is: ", order, option)
    else:
        print("Order is: ", order)
"""
order_size = "Large"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order is:", coffee)