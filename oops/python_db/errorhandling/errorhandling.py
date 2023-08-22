num1=int(input("enter value for number1"))
num2=int(input("enter the value of num2"))

try:
    res=num1/num2
    print("result",res)
except Exception as e:

    print("exception occured")