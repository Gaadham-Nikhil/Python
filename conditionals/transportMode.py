distance = 2;

if distance < 3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
elif distance > 15:
    mode = "car"

print(mode)