password = "harsh"

length = len(password)

if length < 6:
    strength = "weak"
elif length <= 10:
    strength = "medium"
else:
    strength = "strong"

print("password strength is: ",strength)