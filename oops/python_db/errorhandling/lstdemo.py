lst=[10,20,30,40,50]
location=int(input("Enter location tp fetch value:"))
try:
    print(lst[location])
except Exception as e:
    print(e.args)
finally:
    print("dbcommit")
    print("file read")