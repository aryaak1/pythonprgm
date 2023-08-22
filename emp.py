employee={"id":100,"name":"vijay","department":"hr","salary":250000}

#create a function for returning employee name

# def get_name(emp):
#     return emp.get("name")
# print(get_name(employee))


#create a lambda function for returning employee salary

# emp_salary=lambda emp:emp.get("salary")
# print(emp_salary(employee))

def addition(*args):
    return sum(args)

print(addition(10,20))
print(addition(10,20,30))

addition=lambda *args:sum(args)
print(addition(1,2,3,4,5,6,7,8))

def maximum(*args):
    return max(args)
print(maximum(1,2,3,4,5,6,7,8,33,12))

maximum=lambda *args:max(args)
print(maximum(12,34,56,77,89,98,76,55))
