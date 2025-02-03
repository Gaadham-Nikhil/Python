def kwargs_fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print(" ")
kwargs_fun(name = "person", work = "microsoft")
print(" ")
kwargs_fun(name = "nikhil")
print(" ")
kwargs_fun(name = "omkar", work = "startup", role = "flutter")
