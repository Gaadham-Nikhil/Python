number = 5

for i in range (1, 10+1):
    if i == 5:
        continue
    answer = number * i
    print(number, ' X', i, ' = ', answer)