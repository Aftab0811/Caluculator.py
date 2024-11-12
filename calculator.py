print("*************CALCULATOR*************")
operator = input ("Enter an oprator(+ - * /):")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))

if operator == "+":
    result = num1 + num2 + num3
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2 - num3
    print(round(result, 3))
elif operator =="*":
    result = num1 * num2 * num3
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2 / num3
    print(round(result, 3))
else:
    print (f"{operator} is not a valid oprator")
print("******THANKS******")
a=input("by the way what is you name:")
print(a,"thanks to use i will wait for you")
