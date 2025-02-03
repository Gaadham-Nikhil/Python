"""
numbers = [1,2,3,4,5,6,7,8]
sum_even = 0
for even in numbers:
    if even % 2 == 0:
        sum_even += even
print("sum of even numbers is: ", sum_even)
"""
n = 8
sum_even = 0
for num in range(0,n+1):
    if num % 2 == 0:
        sum_even += num

print("sum of even numbers is: ",sum_even)