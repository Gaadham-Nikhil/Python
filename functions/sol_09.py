# def even_num(limit):
#     list = []
#     for i in range(2, limit+1, 2):
#         list.append(i)
#     return list

# print(even_num(10))
# THE ABOVE CODE IS RETURNING LIST AND IT IS NOT YIELDING

#------------------------------------------------#

def even_num_gen(limit):
    for i in range(2, limit + 1, 2):
        yield i
    
for num in even_num_gen(10):
    print(num)

# THIS ABOVE CODE YIELDS THE VALUES(GENERATES), SECOND FOR LOOP PRINTS NUMBERS IN LIMIT