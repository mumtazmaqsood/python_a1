
#handle ZeroDivisionError and ValueError
# no1 = int(input("Enter no1:"))
# no2 = int(input("Enter no2:"))
# result = no1 / no2
# print(result)
try:
    no1 = int(input("Enter no1:"))
    no2 = int(input("Enter no2:"))
    resutl = no1 /no2
except ZeroDivisionError:
    print("YOu cannot divide by zero")
except ValueError:
    print("You cannot enter string value")
else:
    print(resutl)

