year = 20

if ((year % 4) == 0) or ((year % 100) != 0) and ((year % 400) == 0):
        print(year, "year is a leap year")
else:
        print("not a leap year")