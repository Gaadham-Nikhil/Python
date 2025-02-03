# var = "Apple"

# def func():
#     var = "Banana"

# print(var)

# output: Apple
#function is never called
#-----------------------------------------------------------------------

print("function - 1")

var = "Apple"

def func1():
    var = "Banana"

print(var)
func1()

#output: Apple 
# Function is called but inside function print statement of char is never written to print banana
#---------------------------------------------------------------------------------

print("function - 2")

var = "Apple"
def func2():
    var = "Banana"
    print(var)

print(var)
func2()

#output: Apple 
#        Banana
# Function is called print statement is written inside function
#---------------------------------------------------------------------------------

print("function - 3")

var = "Apple"
def func3():
    # var = "Banana"
    print(var)

print(var)
func3()

#output: Apple 
#        Apple
# Function is called and in variable var apple string is stored
#---------------------------------------------------------------------------------

print("function - 4")

num = 1
def add(y):
    z = num + y
    return z

result = add(36)
print(result)

#output: 37
#In add function 36 is added with 'y' value 1 and function call is returned adding the result as 37
#---------------------------------------------------------------------------------

print("function - 5")

x = 53
def func4():
    x = 10

func4()
print(x)

#output: 53
# The function func4 is called but inside the function to print 'x' no function is written. So, the global variable x value 53 is printed
#---------------------------------------------------------------------------------

print("function - 5")

x = 53
def func4():
    x = 10
    print(x)

func4()
print(x)

# output: 10
#         53
# The function func4 is called and inside the function the print statement prints x value and the global variable x value prints 53
#---------------------------------------------------------------------------------

print("function - 6")

x = 53
def func4():
    global x
    x = 10

func4()
print(x)

#output: 10
#keyword global overwrites the x value. but usage of This method is not usually recommended
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

# CLOSURE

def f1():
    k = 1

    def f2():
        print(k)

    return f2
myResult = f1()
myResult()

#---------------------------------------------------------------------------------

def var1(num1):
    def actual(p):
        return p ** num1

    return actual
val1 = var1(2)
val2 = var1(3)

print(var1(2)) #2**2 = 4
print(var1(4)) #4**3 = 64