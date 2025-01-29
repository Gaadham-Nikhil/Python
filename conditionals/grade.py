mark = int(input("enter the marks"))

if mark >= 101:
    print("enter valid marks!!!")
    exit()
if mark >= 90:
    print("grade - A")
elif mark >= 80:
    print("grade - B")
elif mark >= 70:
    print("grade - C")
elif mark >= 60:
    print("grade - D")
else:
    print("grade - F")